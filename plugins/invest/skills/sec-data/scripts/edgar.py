#!/usr/bin/env python3
"""Read-only helper for SEC EDGAR. Standard library only, no API key.

  edgar.py filings TICKER [TICKER ...] [--forms 10-Q,10-K,8-K] [--since YYYY-MM-DD] [--limit 8]
  edgar.py facts TICKER
  edgar.py exhibits TICKER ACCESSION
  edgar.py text URL --out FILE

SEC's fair-access rule asks every program to name itself and give a contact
email. Pass --contact you@example.com, or set HOMEBASE_CONTACT. The email goes
to sec.gov only, in the request header, and nowhere else.
"""
import argparse
import datetime as dt
import html
import json
import os
import re
import sys
import tempfile
import time
import urllib.error
import urllib.request

TICKERS_URL = "https://www.sec.gov/files/company_tickers.json"
SUBMISSIONS = "https://data.sec.gov/submissions/CIK{cik:010d}.json"
FACTS = "https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json"
ARCHIVE = "https://www.sec.gov/Archives/edgar/data/{cik}/{acc}/"

# Each line: label, kind, candidate XBRL tags (companies choose different ones).
METRICS = [
    ("Revenue", "flow", ["RevenueFromContractWithCustomerExcludingAssessedTax", "Revenues", "RevenuesNetOfInterestExpense",
                         "SalesRevenueNet", "RevenueFromContractWithCustomerIncludingAssessedTax"]),
    ("Gross profit", "flow", ["GrossProfit"]),
    ("Operating income", "flow", ["OperatingIncomeLoss"]),
    ("Net income", "flow", ["NetIncomeLoss", "ProfitLoss"]),
    ("Diluted EPS", "flow_eps", ["EarningsPerShareDiluted"]),
    ("Operating cash flow", "ytd", ["NetCashProvidedByUsedInOperatingActivities"]),
    ("Capital spending", "ytd", ["PaymentsToAcquirePropertyPlantAndEquipment",
                                 "PaymentsToAcquireProductiveAssets"]),
    ("Cash and equivalents", "instant", ["CashAndCashEquivalentsAtCarryingValue",
                                         "CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents"]),
    ("Long-term debt", "instant", ["LongTermDebt", "LongTermDebtNoncurrent"]),
    ("Shareholders' equity", "instant", ["StockholdersEquity"]),
    ("Diluted shares", "flow_eps", ["WeightedAverageNumberOfDilutedSharesOutstanding"]),
]

_contact = None
_last_call = 0.0


def get(url):
    """One polite GET: named client, at most about 5 requests a second."""
    global _last_call
    if not _contact:
        sys.exit("SEC asks for a contact email. Pass --contact you@example.com "
                 "or set HOMEBASE_CONTACT. It is sent to sec.gov only.")
    wait = 0.2 - (time.time() - _last_call)
    if wait > 0:
        time.sleep(wait)
    _last_call = time.time()
    req = urllib.request.Request(url, headers={"User-Agent": f"homebase-invest {_contact}"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.read()
    except urllib.error.HTTPError as e:
        sys.exit(f"SEC returned HTTP {e.code} for {url}")
    except urllib.error.URLError as e:
        sys.exit(f"Could not reach sec.gov ({e.reason}). No data was read.")


def cik_for(ticker):
    cache = os.path.join(tempfile.gettempdir(), "homebase_sec_tickers.json")
    fresh = os.path.exists(cache) and time.time() - os.path.getmtime(cache) < 7 * 86400
    if fresh:
        raw = open(cache, "rb").read()
    else:
        raw = get(TICKERS_URL)
        try:
            open(cache, "wb").write(raw)
        except OSError:
            pass
    want = ticker.upper().replace(".", "-")
    for row in json.loads(raw).values():
        if row["ticker"].upper() == want:
            return int(row["cik_str"]), row["title"]
    sys.exit(f"{ticker}: not found in SEC's ticker list. Funds, ETFs and foreign "
             f"listings often are not there. Nothing was guessed.")


def cmd_filings(args):
    forms = {f.strip().upper() for f in args.forms.split(",")} if args.forms else None
    for ticker in args.tickers:
        cik, name = cik_for(ticker)
        recent = json.loads(get(SUBMISSIONS.format(cik=cik)))["filings"]["recent"]
        print(f"## {ticker.upper()} ({name}, CIK {cik})")
        shown = 0
        for i, form in enumerate(recent["form"]):
            if forms and form.upper() not in forms:
                continue
            filed = recent["filingDate"][i]
            if args.since and filed < args.since:
                break  # newest first
            acc = recent["accessionNumber"][i]
            base = ARCHIVE.format(cik=cik, acc=acc.replace("-", ""))
            items = recent.get("items", [""] * (i + 1))[i]
            note = " (earnings release)" if form == "8-K" and "2.02" in items else ""
            period = recent["reportDate"][i] or "n/a"
            print(f"- {filed} | {form}{note} | period {period} | {acc}\n  {base}{recent['primaryDocument'][i]}")
            shown += 1
            if shown >= args.limit:
                break
        if not shown:
            print("- none in that window")
        print()


def _days(row):
    return (dt.date.fromisoformat(row["end"]) - dt.date.fromisoformat(row["start"])).days


def _pick(facts, tags, kind):
    """The candidate tag whose data runs most recently (by quarter, for quarterly lines)."""
    best, best_end = None, ""
    for tag in tags:
        node = facts.get("us-gaap", {}).get(tag)
        if not node:
            continue
        for unit, rows in node["units"].items():
            ends = [r["end"] for r in rows
                    if not kind.startswith("flow") or ("start" in r and 80 <= _days(r) <= 100)]
            end = max(ends or [min(r["end"] for r in rows)])
            if end > best_end:
                best, best_end = (tag, unit, rows), end
    return best


def _latest_by_period(rows, key):
    out = {}
    for r in sorted(rows, key=lambda r: r.get("filed", "")):
        out[key(r)] = r  # a later filing replaces an earlier one (restatements)
    return out


def _fmt(val, unit):
    if unit.startswith("USD/"):
        return f"{val:.2f}"
    for size, tag in ((1e9, "B"), (1e6, "M")):
        if abs(val) >= size:
            return f"{val / size:,.2f}{tag}"
    return f"{val:,.0f}"


def cmd_facts(args):
    cik, name = cik_for(args.ticker)
    facts = json.loads(get(FACTS.format(cik=cik))).get("facts", {})
    if "us-gaap" not in facts:
        sys.exit(f"{args.ticker}: no US-GAAP data at SEC (foreign filers report differently). "
                 f"Read the filing itself instead.")
    print(f"# {args.ticker.upper()} ({name}) as reported to the SEC")
    print("Source: SEC XBRL company facts. Q4 is not filed separately; where shown it is "
          "the full year minus the first three quarters and is marked (derived).\n")
    for label, kind, tags in METRICS:
        picked = _pick(facts, tags, kind)
        if not picked:
            print(f"**{label}:** not reported under the usual tags\n")
            continue
        tag, unit, rows = picked
        print(f"**{label}** ({tag}, {unit})")
        if kind == "instant":
            pts = _latest_by_period(rows, lambda r: r["end"])
            for end in sorted(pts)[-6:]:
                print(f"- {end}: {_fmt(pts[end]['val'], unit)}")
        else:
            rows = [r for r in rows if "start" in r]
            per = _latest_by_period(rows, lambda r: (r["start"], r["end"]))
            quarters = {k: v for k, v in per.items() if 80 <= _days(v) <= 100}
            years = {k: v for k, v in per.items() if 350 <= _days(v) <= 380}
            if kind == "ytd":
                ytd = {k: v for k, v in per.items() if 80 <= _days(v) <= 290}
                for k in sorted(ytd, key=lambda k: k[1])[-4:]:
                    print(f"- {k[0]} to {k[1]} (year to date): {_fmt(ytd[k]['val'], unit)}")
            else:
                if kind == "flow":  # derive Q4 only for amounts that add up
                    for (ys, ye), yrow in years.items():
                        inside = [v for (s, e), v in quarters.items() if s >= ys and e <= ye]
                        if len(inside) == 3:
                            last_end = max(v["end"] for v in inside)
                            start = (dt.date.fromisoformat(last_end) + dt.timedelta(days=1)).isoformat()
                            quarters.setdefault((start, ye), {
                                "val": yrow["val"] - sum(v["val"] for v in inside),
                                "start": start, "end": ye, "derived": True})
                newest = max(r["end"] for r in rows)
                cutoff = (dt.date.fromisoformat(newest) - dt.timedelta(days=800)).isoformat()
                quarters = {k: v for k, v in quarters.items() if k[1] >= cutoff}
                if not quarters:
                    print("- no recent quarterly values under this tag; read them from the filing")
                for k in sorted(quarters, key=lambda k: k[1])[-8:]:
                    mark = " (derived)" if quarters[k].get("derived") else ""
                    print(f"- quarter ended {k[1]}: {_fmt(quarters[k]['val'], unit)}{mark}")
            for k in sorted(years, key=lambda k: k[1])[-3:]:
                print(f"- year ended {k[1]}: {_fmt(years[k]['val'], unit)}")
        print()


def cmd_exhibits(args):
    cik, _ = cik_for(args.ticker)
    base = ARCHIVE.format(cik=cik, acc=args.accession.replace("-", ""))
    listing = json.loads(get(base + "index.json"))
    for item in listing["directory"]["item"]:
        name = item["name"]
        if name.lower().endswith((".htm", ".html", ".txt", ".pdf")):
            print(f"- {name} ({item.get('size') or '?'} bytes)\n  {base}{name}")


def cmd_text(args):
    if not re.match(r"https://(www|data)\.sec\.gov/", args.url):
        sys.exit("This command only reads sec.gov addresses.")
    raw = get(args.url).decode("utf-8", "replace")
    raw = re.sub(r"(?is)<(script|style|ix:header).*?</\1>", " ", raw)
    raw = re.sub(r"(?i)<(br|/p|/div|/tr|/h[1-6]|/li)[^>]*>", "\n", raw)
    raw = re.sub(r"(?i)</t[dh]>", " | ", raw)
    text = html.unescape(re.sub(r"<[^>]+>", "", raw)).replace("\xa0", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n\s*\n+", "\n\n", text).strip()
    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write(text)
    lines = text.count("\n") + 1
    print(f"Saved {len(text):,} characters, {lines:,} lines to {args.out}")
    for m in re.finditer(r"(?im)^\s*item\s+\d+[a-z]?\.?[^\n]{0,80}$", text):
        print(f"  line {text.count(chr(10), 0, m.start()) + 1}: {m.group().strip()[:90]}")


def main():
    global _contact
    p = argparse.ArgumentParser(description="Read-only SEC EDGAR helper.")
    p.add_argument("--contact", default=os.environ.get("HOMEBASE_CONTACT"))
    sub = p.add_subparsers(dest="cmd", required=True)
    f = sub.add_parser("filings")
    f.add_argument("tickers", nargs="+")
    f.add_argument("--forms", default="10-Q,10-K,8-K")
    f.add_argument("--since")
    f.add_argument("--limit", type=int, default=8)
    f.set_defaults(fn=cmd_filings)
    x = sub.add_parser("facts")
    x.add_argument("ticker")
    x.set_defaults(fn=cmd_facts)
    e = sub.add_parser("exhibits")
    e.add_argument("ticker")
    e.add_argument("accession")
    e.set_defaults(fn=cmd_exhibits)
    t = sub.add_parser("text")
    t.add_argument("url")
    t.add_argument("--out", required=True)
    t.set_defaults(fn=cmd_text)
    args = p.parse_args()
    _contact = args.contact
    args.fn(args)


if __name__ == "__main__":
    main()
