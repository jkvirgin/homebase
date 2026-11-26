---
name: brief
description: The reader's stock brief, one page on the companies they follow and own. Use for "my brief", "weekly brief", "what happened with my stocks", "anything new on my watchlist", "catch me up on my stocks", or a scheduled weekly run.
---

# Weekly brief

One page the reader can act on without opening anything else. It is a snapshot of where things stand, complete by itself, never "what changed since last time".

## Steps

1. Find the Homebase folder: the current folder if it contains `invest/watchlist.md`, otherwise `~/Documents/Homebase`. Check those two places only; do not search the whole computer. If neither has it, run the `setup` skill and stop.
2. Read `invest/watchlist.md`, `invest/holdings.csv` if present, `invest/settings.md` and `invest/lessons.md`. Note the date of the newest file in `invest/briefs/`; the window is from that date to today, or the last 7 days if there is none.
3. New filings in the window: use the `sec-data` skill, `filings` for every ticker in one call with `--since`.
4. Prices: the `sec-data` skill's `prices` command for every ticker in one call, with `--since` set to the start of the window.
5. News: web search per company, by ticker and name only. Keep only news that changes the picture: results, guidance, deals, leadership, lawsuits, regulators, dividend changes. Skip analyst chatter and price-target notes.
6. Upcoming: the next earnings date for each company, from the company's investor page or a named site. Mark a date "expected" unless the company has confirmed it.
7. Save the brief to `invest/briefs/YYYY-MM-DD.md`, then show it.

## Shape

```
# Brief: <Weekday, Month D, YYYY>

**In one line:** <the most important thing this week, or "A quiet week.">

## Needs a look
- <TICKER>: <what happened, the number, the source and date>. <Why it matters to this reader.>

## What you own            (only if holdings.csv exists)
| Ticker | Close | Week | Since you bought | Note |

## Watchlist
| Ticker | Close | Week | Note |

## Coming up
- <Weekday, date>: <TICKER> reports <quarter> (confirmed / expected)

## New filings
- <TICKER> <form> filed <date>: <one line>. Say "analyze <TICKER>'s quarter" for the full read.

Sources: <site and date for prices; SEC EDGAR for filings>
```

- "Needs a look" holds at most five items and may be empty. A quiet week is a fine answer; do not pad it.
- When a 10-Q, 10-K or earnings release landed in the window, offer the `quarterly-report` skill; do not run it inside the brief.
- Keep the brief under about 400 words unless `settings.md` asks for detail.
- If a price could not be found for a ticker, put "not found" in the cell.

## House rules (every answer)

- Answer first in one or two lines, then short bullets. No long paragraphs.
- Every number names its source and its date: the filing and period, or the site and the day.
- If you could not find something, say "not found". Never estimate a reported number.
- Say plainly when data is a day old, delayed or derived.
- Read-only. Never log in to a brokerage, never place or prepare a trade, never say buy, sell or hold. Lay out the facts and what would have to be true; the decision is the reader's.
- Write dates with the day of the week. Check today's date before you write it.
- Read `invest/lessons.md` in the Homebase folder before you start and follow it. When the reader corrects you or states a preference, add one line to it.
