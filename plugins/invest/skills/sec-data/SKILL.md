---
name: sec-data
description: Get a US company's SEC filings and reported financial numbers from EDGAR, and end-of-day share prices, free and with no API key. Use whenever a skill or question needs a 10-Q, 10-K, 8-K earnings release, a list of recent filings, reported figures such as revenue, net income, EPS, cash or debt, or a stock's latest close and recent change.
user-invocable: false
---

# SEC data

SEC EDGAR is the source of record. Prefer it over any news site for a reported number.

## Path A: the helper script (use when you can run python3 and reach sec.gov)

Read `sec_contact` from `invest/settings.md` in the Homebase folder and pass it as `--contact`. If it is `none` or missing, use Path B. Do not make up an address and do not use any other email.

```
python3 ${CLAUDE_SKILL_DIR}/scripts/edgar.py --contact EMAIL filings AAPL MSFT --since 2026-01-01
python3 ${CLAUDE_SKILL_DIR}/scripts/edgar.py --contact EMAIL facts AAPL
python3 ${CLAUDE_SKILL_DIR}/scripts/edgar.py --contact EMAIL exhibits AAPL 0000320193-26-000024
python3 ${CLAUDE_SKILL_DIR}/scripts/edgar.py --contact EMAIL text <sec.gov URL> --out invest/filings/AAPL-10Q-2026-06-27.txt
```

If `${CLAUDE_SKILL_DIR}` shows above as literal text, the script is `scripts/edgar.py` next to this file.

- `filings`: recent 10-Q, 10-K and 8-K with dates, periods and links. An 8-K marked "(earnings release)" carries the press release as an exhibit.
- `facts`: revenue, gross profit, operating income, net income, diluted EPS, cash flow, cash, debt, equity and share count for recent quarters and years, exactly as filed. Lines marked "(derived)" are arithmetic, not filed figures; say so when you quote them.
- `exhibits`: the files inside one filing. The earnings press release is usually the one with `ex99` in its name.
- `text`: saves a filing as plain text and prints where each Item starts. Then read only the part you need (for a 10-Q, "Management's Discussion and Analysis"; search for that phrase). Do not read a whole filing into the conversation.

If `python3` is missing, do not install anything. Use Path B.

## Path B: web fetch (no script)

- Ticker to CIK: `https://www.sec.gov/files/company_tickers.json`
- Filing list: `https://data.sec.gov/submissions/CIK##########.json` (CIK padded to 10 digits)
- One reported figure: `https://data.sec.gov/api/xbrl/companyconcept/CIK##########/us-gaap/<Tag>.json`, for example `NetIncomeLoss`, `Revenues`, `EarningsPerShareDiluted`
- These files are long and a fetch may cut them off. If the part you need is missing, say so; do not fill the gap from memory.
- `sec.gov/cgi-bin/browse-edgar` and the full-text search do not work through web fetch. Do not try them.

## Path C: the company's own investor relations page

Use web search to find the earnings press release and 10-Q on the company's investor site. Name the page and its date as the source.

## Share prices

```
python3 ${CLAUDE_SKILL_DIR}/scripts/edgar.py prices AAPL MSFT --since 2026-11-19
```

- Gives the latest close and its date, and the change since a date, over 30 days and over a year. No contact email is needed and only the ticker is sent.
- The source is public quote data (Yahoo Finance, then Nasdaq), not the SEC. It is end-of-day, unofficial, and can stop working. Always name the source and the close date beside a price.
- If it prints "not found", or the script cannot run, use web search and name the site and date. If that fails too, write "not found".
- Never send share counts, dollar amounts or anything else about the reader with a price lookup.

## Limits to state when they apply

- Foreign companies (20-F and 6-K filers such as TSM) and funds have no figures in `facts`. Read their filing or release instead.
- EDGAR has no share prices. See "Share prices" below.
- If all three paths fail, report "could not reach the filing" and stop. Never reconstruct figures from memory.
