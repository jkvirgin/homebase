---
name: portfolio
description: The reader's own holdings. Add or update what they own, import a brokerage export file, and show value, gain or loss and concentration. Use for "how is my portfolio", "what do I own", "I bought", "I sold", "update my holdings", "import my positions".
---

# Portfolio

A record the reader keeps, in `invest/holdings.csv` in the Homebase folder. It is typed in or imported from a file they export themselves.

## Hard limits

- Never ask for, accept or use a brokerage username, password, security code or account number. If the reader offers one, decline and explain that the file export does the job.
- Never connect to a brokerage. Never place, draft or stage a trade.
- Holdings are private. They stay in `holdings.csv`. Do not put share counts or dollar amounts in a web search or any request to an outside site; search by ticker only.

## The file

```
ticker,shares,cost_per_share,bought,account,notes
AAPL,50,142.10,2021-03-15,IRA,
```

- One row per lot. `account` is a label the reader chooses ("IRA", "Joint"), never an account number.
- Before changing the file, copy it to `invest/holdings.backup.csv`.

## Updating

- "I bought 20 MSFT at 410": add a row. "I sold 10 AAPL": reduce the oldest lot unless they name one. Read the change back in one line before saving.
- Import: the reader exports positions from their brokerage site (usually "Positions" then "Export" or "Download CSV") and puts the file in the Homebase folder. Read it, map its columns, show the rows you will write, and save only after they say yes. Drop any account-number column. Leave the export file where it is and suggest they delete it.

## Showing it

1. Latest close for each ticker by web search, with the site and date named.
2. Compute per holding: value, gain or loss in dollars and percent, share of the whole.

```
# Portfolio: <Weekday, Month D, YYYY>
**In one line:** <total value, total gain or loss, biggest mover>

| Ticker | Shares | Cost | Close | Value | Gain/loss | % of total |

## Worth knowing
- Concentration: <any holding over 20% of the total; top three together>
- <anything in the watchlist files that bears on a holding: results due, a new filing>

Prices: <site>, close of <date>. Values are computed from your holdings file.
```

- Cash, funds and anything with no price found: list it, mark the price "not found", and leave it out of the totals with a note.
- This is arithmetic on the reader's own records. It is not tax advice and not a brokerage statement; say so once if they ask about taxes.

## House rules (every answer)

- Answer first in one or two lines, then short bullets. No long paragraphs.
- Every number names its source and its date: the filing and period, or the site and the day.
- If you could not find something, say "not found". Never estimate a reported number.
- Say plainly when data is a day old, delayed or derived.
- Read-only. Never log in to a brokerage, never place or prepare a trade, never say buy, sell or hold. Lay out the facts and what would have to be true; the decision is the reader's.
- Write dates with the day of the week. Check today's date before you write it.
- Read `invest/lessons.md` in the Homebase folder before you start and follow it. When the reader corrects you or states a preference, add one line to it.
