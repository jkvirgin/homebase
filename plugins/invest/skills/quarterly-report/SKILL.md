---
name: quarterly-report
description: Analyze a company's latest quarterly or annual results from its SEC filing and earnings release, in one fixed format. Use for "analyze <company>'s quarter", "how were <company>'s earnings", "read the 10-Q", "read the 10-K", "what did <company> report".
argument-hint: "[ticker or company]"
---

# Quarterly report

Read what the company filed, and say what it means in plain words. The same shape every time, so one quarter can be laid beside the last.

## Steps

1. Confirm the company and ticker. Find the Homebase folder; read `invest/lessons.md` and `invest/settings.md`.
2. With the `sec-data` skill:
   - `filings` for the ticker. Pick the newest 10-Q or 10-K, and the 8-K marked "(earnings release)" from the same days.
   - `facts` for the numbers.
   - `exhibits` on the earnings 8-K, then `text` on the press release exhibit (`ex99`).
   - `text` on the 10-Q or 10-K, then read only Management's Discussion and Analysis, and skim Risk Factors and Legal Proceedings for anything new.
3. If an earlier analysis of this company is in `invest/reports/`, read the latest one so "what changed" compares like with like.
4. Check each figure you quote against `facts` or the filing text. A figure you cannot find in either does not go in the report.
5. Save to `invest/reports/<TICKER>-<period end YYYY-MM-DD>.md`, then show it.

## Shape

```
# <Company> (<TICKER>): quarter ended <date>
Filed <Weekday, date>. Sources: <form and link>, <press release link>.

**In one line:** <what kind of quarter it was and the one thing that mattered>

## The numbers
| | This quarter | A year ago | Change | Last quarter |
| Revenue | | | | |
| Gross margin | | | | |
| Operating income | | | | |
| Operating margin | | | | |
| Net income | | | | |
| Diluted EPS | | | | |
| Operating cash flow (year to date) | | | | |
| Cash | | | | |
| Long-term debt | | | | |
| Diluted shares | | | | |

## What drove it
- <3 to 5 bullets from management's discussion: segments, prices, volumes, costs, one-offs>

## What management said about what is next
- <guidance and outlook, in their words where short; "No guidance given." if none>

## What changed since last quarter
- <better, worse, new, gone>

## Things to watch
- <red flags and open questions: one-time items, rising debt, falling cash, share count, new risks, legal matters, accounting changes>

## What would have to be true
- For this to be going well: <2 or 3 conditions>
- For this to be going badly: <2 or 3 conditions>
```

- Margins are computed from filed figures; say "computed".
- Compare a quarter with the same quarter a year ago first, because many businesses are seasonal.
- Banks, insurers and REITs do not report gross margin or operating income the usual way. Replace those rows with the measures the company itself leads with, and say you did.
- If the 10-Q is not filed yet and only the press release is out, say so at the top and mark the report "from the press release; the full filing is not out".
- No price target, no rating, no buy or sell.

## House rules (every answer)

- Answer first in one or two lines, then short bullets. No long paragraphs.
- Every number names its source and its date: the filing and period, or the site and the day.
- If you could not find something, say "not found". Never estimate a reported number.
- Say plainly when data is a day old, delayed or derived.
- Read-only. Never log in to a brokerage, never place or prepare a trade, never say buy, sell or hold. Lay out the facts and what would have to be true; the decision is the reader's.
- Write dates with the day of the week. Check today's date before you write it.
- Read `invest/lessons.md` in the Homebase folder before you start and follow it. When the reader corrects you or states a preference, add one line to it.
