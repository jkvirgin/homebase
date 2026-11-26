#!/usr/bin/env python3
"""The trainer's logbook: plain CSV files in the reader's own folder. Standard library only.

  trainer.py set "<movement>" [--load N] [--unit lb|kg|bodyweight] [--reps N | --seconds N] [--effort 1-10]
                 [--kind warmup|working] [--note T] [--date D]
  trainer.py cardio "<activity>" --minutes N [--distance N] [--unit mi|km] [--effort 1-10] [--note T] [--date D]
  trainer.py food "<what>" [--kcal N --protein N --carbs N --fat N] [--meal M] [--estimate] [--note T] [--date D]
  trainer.py body [--weight N] [--waist N] [--bp 120/80] [--resting-hr N] [--note T] [--date D]
  trainer.py sleep --hours N [--quality 1-5] [--note T] [--date D]
  trainer.py note <feel|pain|mobility|water|habit|other> "<text>" [--date D]
  trainer.py usual add "<name>" --kcal N --protein N [--carbs N --fat N] | usual list | usual remove "<name>"
  trainer.py today [--date D]            everything logged that day, with row numbers
  trainer.py last "<movement>"           the last three days that movement was done, and the best
  trainer.py week [--date D]             the last 7 days against the targets in profile.md
  trainer.py history <sets|cardio|food|body|sleep|notes> [--days N]
  trainer.py undo <sets|cardio|food|body|sleep|notes>      remove the newest row of that kind

The folder is --dir, or $HOMEBASE_TRAINER, or ~/Homebase/trainer. Nothing leaves it.
"""
import argparse
import csv
import datetime as dt
import os
import re
import sys

FILES = {
    "sets": ["date", "movement", "kind", "load", "unit", "reps", "seconds", "effort", "note"],
    "cardio": ["date", "activity", "minutes", "distance", "unit", "effort", "note"],
    "food": ["date", "meal", "what", "kcal", "protein", "carbs", "fat", "estimate", "note"],
    "body": ["date", "weight", "waist", "bp", "resting_hr", "note"],
    "sleep": ["date", "hours", "quality", "note"],
    "notes": ["date", "kind", "text"],
    "usuals": ["name", "kcal", "protein", "carbs", "fat"],
}
DIR = None


def path(name):
    return os.path.join(DIR, f"{name}.csv")


def rows(name):
    if not os.path.exists(path(name)):
        return []
    with open(path(name), newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def write(name, data):
    os.makedirs(DIR, exist_ok=True)
    with open(path(name), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=FILES[name])
        w.writeheader()
        w.writerows(data)


def add(name, row):
    os.makedirs(DIR, exist_ok=True)
    new = not os.path.exists(path(name))
    with open(path(name), "a", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=FILES[name])
        if new:
            w.writeheader()
        row = {k: (int(v) if isinstance(v, float) and v.is_integer() else v) for k, v in row.items()}
        w.writerow({k: ("" if row.get(k) is None else row.get(k)) for k in FILES[name]})
    shown = ", ".join(f"{k} {v}" for k, v in row.items() if v not in (None, "") and k != "date")
    print(f"Logged for {day_name(row.get('date'))}: {shown}" if "date" in row else f"Saved: {shown}")


def the_date(text):
    if not text or text == "today":
        return dt.date.today().isoformat()
    if text == "yesterday":
        return (dt.date.today() - dt.timedelta(days=1)).isoformat()
    try:
        return dt.date.fromisoformat(text).isoformat()
    except ValueError:
        sys.exit(f"Date '{text}' is not understood. Use YYYY-MM-DD, today or yesterday. Nothing was logged.")


def day_name(iso):
    d = dt.date.fromisoformat(iso)
    return f"{d.strftime('%A, %B')} {d.day}, {d.year}"


def num(text):
    try:
        return float(text)
    except (TypeError, ValueError):
        return 0.0


def same(a, b):
    def norm(s):
        return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()
    return norm(a) == norm(b)


def targets():
    """Lines like `protein_g: 120` under any heading in profile.md."""
    out = {}
    p = os.path.join(DIR, "profile.md")
    if os.path.exists(p):
        for line in open(p, encoding="utf-8"):
            m = re.match(r"\s*-?\s*([a-z_]+)\s*:\s*([0-9.]+)\s*$", line)
            if m:
                out[m.group(1)] = float(m.group(2))
    return out


def cmd_set(a):
    add("sets", {"date": the_date(a.date), "movement": a.movement, "kind": a.kind, "load": a.load, "unit": a.unit,
                 "reps": a.reps, "seconds": a.seconds, "effort": a.effort, "note": a.note})


def cmd_cardio(a):
    add("cardio", {"date": the_date(a.date), "activity": a.activity, "minutes": a.minutes, "distance": a.distance,
                   "unit": a.unit if a.distance else None, "effort": a.effort, "note": a.note})


def cmd_food(a):
    row = {"date": the_date(a.date), "meal": a.meal, "what": a.what, "kcal": a.kcal, "protein": a.protein,
           "carbs": a.carbs, "fat": a.fat, "estimate": "yes" if a.estimate else "", "note": a.note}
    if a.kcal is None and a.protein is None:
        usual = next((u for u in rows("usuals") if same(u["name"], a.what)), None)
        if not usual:
            sys.exit(f"'{a.what}' is not a usual food, so give --kcal and --protein (add --estimate if they are "
                     f"estimates). Nothing was logged.")
        row.update({k: usual[k] for k in ("kcal", "protein", "carbs", "fat")})
    add("food", row)


def cmd_body(a):
    if not any([a.weight, a.waist, a.bp, a.resting_hr]):
        sys.exit("Give at least one of --weight, --waist, --bp, --resting-hr. Nothing was logged.")
    add("body", {"date": the_date(a.date), "weight": a.weight, "waist": a.waist, "bp": a.bp,
                 "resting_hr": a.resting_hr, "note": a.note})


def cmd_sleep(a):
    add("sleep", {"date": the_date(a.date), "hours": a.hours, "quality": a.quality, "note": a.note})


def cmd_note(a):
    add("notes", {"date": the_date(a.date), "kind": a.kind, "text": a.text})


def cmd_usual(a):
    data = rows("usuals")
    if a.action == "list":
        if not data:
            print("No usual foods saved yet.")
        for u in data:
            print(f"- {u['name']}: {u['kcal']} kcal, {u['protein']} g protein, {u['carbs'] or '?'} g carbs, {u['fat'] or '?'} g fat")
        return
    if not a.name:
        sys.exit("Give the food's name.")
    kept = [u for u in data if not same(u["name"], a.name)]
    if a.action == "remove":
        write("usuals", kept)
        print(f"Removed '{a.name}'." if len(kept) < len(data) else f"'{a.name}' was not in the list.")
        return
    if a.kcal is None or a.protein is None:
        sys.exit("A usual food needs --kcal and --protein. Nothing was saved.")
    kept.append({k: (int(v) if isinstance(v, float) and v.is_integer() else v) for k, v in
                 {"name": a.name, "kcal": a.kcal, "protein": a.protein, "carbs": a.carbs, "fat": a.fat}.items()})
    write("usuals", kept)
    print(f"Saved usual food '{a.name}': {a.kcal} kcal, {a.protein} g protein.")


def show_day(day):
    print(f"# {day_name(day)}")
    any_rows = False
    for name in ("sets", "cardio", "food", "body", "sleep", "notes"):
        todays = [(i + 1, r) for i, r in enumerate(rows(name)) if r["date"] == day]
        if not todays:
            continue
        any_rows = True
        print(f"\n## {name}")
        for i, r in todays:
            print(f"- row {i}: " + ", ".join(f"{k} {v}" for k, v in r.items() if v and k != "date"))
        if name == "food":
            tot = {k: sum(num(r[k]) for _, r in todays) for k in ("kcal", "protein", "carbs", "fat")}
            est = " (includes estimates)" if any(r["estimate"] for _, r in todays) else ""
            print(f"- total: {tot['kcal']:.0f} kcal, {tot['protein']:.0f} g protein, {tot['carbs']:.0f} g carbs, {tot['fat']:.0f} g fat{est}")
    if not any_rows:
        print("Nothing logged.")


def cmd_today(a):
    show_day(the_date(a.date))


def cmd_last(a):
    mine = [r for r in rows("sets") if same(r["movement"], a.movement)]
    if not mine:
        known = sorted({r["movement"] for r in rows("sets")})
        print(f"No sets logged for '{a.movement}'." + (f" Logged movements: {', '.join(known)}." if known else ""))
        return
    days = sorted({r["date"] for r in mine})[-3:]
    for d in days:
        print(f"## {day_name(d)}")
        for r in mine:
            if r["date"] == d:
                amount = f"{r['reps']} reps" if r["reps"] else f"{r['seconds']} s"
                load = "bodyweight" if r["unit"] == "bodyweight" and not r["load"] else f"{r['load']} {r['unit']}".strip()
                extra = "".join([f", effort {r['effort']}" if r["effort"] else "", f", {r['note']}" if r["note"] else ""])
                print(f"- {r['kind'] or 'working'}: {load} x {amount}{extra}")
    working = [r for r in mine if (r["kind"] or "working") == "working" and r["load"] and r["reps"]]
    if working:
        best = max(working, key=lambda r: (num(r["load"]), num(r["reps"])))
        print(f"\nHeaviest working set on record: {best['load']} {best['unit']} x {best['reps']} on {best['date']}.")


def cmd_week(a):
    end = dt.date.fromisoformat(the_date(a.date))
    days = [(end - dt.timedelta(days=i)).isoformat() for i in range(6, -1, -1)]
    t = targets()
    print(f"# Seven days ending {day_name(days[-1])}\n")

    def line(label, value, key=None, unit=""):
        goal = f" (target {t[key]:g}{unit})" if key and key in t else ""
        print(f"- {label}: {value}{goal}")

    sets = [r for r in rows("sets") if r["date"] in days]
    line("Strength days", len({r["date"] for r in sets}), "strength_days")
    cardio = [r for r in rows("cardio") if r["date"] in days]
    line("Cardio minutes", f"{sum(num(r['minutes']) for r in cardio):.0f} over {len({r['date'] for r in cardio})} days", "cardio_minutes")
    food = [r for r in rows("food") if r["date"] in days]
    fdays = sorted({r["date"] for r in food})
    if fdays:
        line("Protein, average on logged days", f"{sum(num(r['protein']) for r in food) / len(fdays):.0f} g ({len(fdays)} of 7 days logged)", "protein_g", " g")
        line("Calories, average on logged days", f"{sum(num(r['kcal']) for r in food) / len(fdays):.0f}", "calories")
    else:
        line("Food", "nothing logged")
    sleep = [r for r in rows("sleep") if r["date"] in days]
    line("Sleep, average", f"{sum(num(r['hours']) for r in sleep) / len(sleep):.1f} h over {len(sleep)} nights" if sleep else "nothing logged", "sleep_hours", " h")
    body = [r for r in rows("body") if r["weight"]]
    if body:
        latest = body[-1]
        before = [r for r in body if r["date"] < days[0]]
        change = f", {num(latest['weight']) - num(before[-1]['weight']):+.1f} since {before[-1]['date']}" if before else ""
        line("Weight", f"{latest['weight']} on {latest['date']}{change}")
    notes = [r for r in rows("notes") if r["date"] in days]
    for kind in ("pain", "feel", "mobility", "habit"):
        mine = [r for r in notes if r["kind"] == kind]
        if mine:
            print(f"- {kind.capitalize()} notes: " + " | ".join(f"{r['date'][5:]}: {r['text']}" for r in mine))
    if not t:
        print("\nNo targets found in profile.md, so none are shown.")


def cmd_history(a):
    cutoff = (dt.date.today() - dt.timedelta(days=a.days)).isoformat()
    mine = [r for r in rows(a.what) if r["date"] >= cutoff]
    if not mine:
        print(f"Nothing in {a.what} in the last {a.days} days.")
    for r in mine:
        print(f"- {r['date']}: " + ", ".join(f"{k} {v}" for k, v in r.items() if v and k != "date"))


def cmd_undo(a):
    data = rows(a.what)
    if not data:
        sys.exit(f"Nothing in {a.what} to remove.")
    gone = data.pop()
    write(a.what, data)
    print("Removed: " + ", ".join(f"{k} {v}" for k, v in gone.items() if v))


def main():
    global DIR
    p = argparse.ArgumentParser(description="Trainer logbook.")
    p.add_argument("--dir", default=os.environ.get("HOMEBASE_TRAINER") or os.path.expanduser("~/Homebase/trainer"))
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("set")
    s.add_argument("movement")
    s.add_argument("--load", type=float)
    s.add_argument("--unit", default="lb", choices=["lb", "kg", "bodyweight"])
    s.add_argument("--reps", type=int)
    s.add_argument("--seconds", type=int)
    s.add_argument("--effort", type=float)
    s.add_argument("--kind", default="working", choices=["warmup", "working"])
    s.set_defaults(fn=cmd_set)

    c = sub.add_parser("cardio")
    c.add_argument("activity")
    c.add_argument("--minutes", type=float, required=True)
    c.add_argument("--distance", type=float)
    c.add_argument("--unit", default="mi", choices=["mi", "km"])
    c.add_argument("--effort", type=float)
    c.set_defaults(fn=cmd_cardio)

    f = sub.add_parser("food")
    f.add_argument("what")
    for k in ("kcal", "protein", "carbs", "fat"):
        f.add_argument(f"--{k}", type=float)
    f.add_argument("--meal")
    f.add_argument("--estimate", action="store_true")
    f.set_defaults(fn=cmd_food)

    b = sub.add_parser("body")
    b.add_argument("--weight", type=float)
    b.add_argument("--waist", type=float)
    b.add_argument("--bp")
    b.add_argument("--resting-hr", type=int, dest="resting_hr")
    b.set_defaults(fn=cmd_body)

    sl = sub.add_parser("sleep")
    sl.add_argument("--hours", type=float, required=True)
    sl.add_argument("--quality", type=int, choices=range(1, 6))
    sl.set_defaults(fn=cmd_sleep)

    n = sub.add_parser("note")
    n.add_argument("kind", choices=["feel", "pain", "mobility", "water", "habit", "other"])
    n.add_argument("text")
    n.set_defaults(fn=cmd_note)

    for sp in (s, c, f, b, sl, n):
        sp.add_argument("--date")
        if sp is not n:
            sp.add_argument("--note")

    u = sub.add_parser("usual")
    u.add_argument("action", choices=["add", "list", "remove"])
    u.add_argument("name", nargs="?")
    for k in ("kcal", "protein", "carbs", "fat"):
        u.add_argument(f"--{k}", type=float)
    u.set_defaults(fn=cmd_usual)

    t = sub.add_parser("today")
    t.add_argument("--date")
    t.set_defaults(fn=cmd_today)
    la = sub.add_parser("last")
    la.add_argument("movement")
    la.set_defaults(fn=cmd_last)
    w = sub.add_parser("week")
    w.add_argument("--date")
    w.set_defaults(fn=cmd_week)
    h = sub.add_parser("history")
    h.add_argument("what", choices=[k for k in FILES if k != "usuals"])
    h.add_argument("--days", type=int, default=30)
    h.set_defaults(fn=cmd_history)
    un = sub.add_parser("undo")
    un.add_argument("what", choices=[k for k in FILES if k != "usuals"])
    un.set_defaults(fn=cmd_undo)

    a = p.parse_args()
    DIR = a.dir
    a.fn(a)


if __name__ == "__main__":
    main()
