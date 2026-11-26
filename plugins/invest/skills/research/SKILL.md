---
name: research
description: Research a company the reader is curious about or considering. Use for "research <company>", "tell me about <company>", "should I look at <company>", "what does <company> do", "compare <company> and <company>".
argument-hint: "[ticker or company]"
---

# Research a company

A first read on a business, from its own filings. It ends with what would have to be true, not with a verdict.

## Steps

1. Confirm which company and ticker; similar names are common. Find the Homebase folder and read `invest/lessons.md`.
2. With the `sec-data` skill: `filings` to find the latest 10-K and 10-Q, `facts` for three years and recent quarters, `text` on the 10-K and read Item 1 (Business), Item 1A (Risk Factors) and the Management's Discussion.
3. Web search for the last six months of news that changes the picture, and the latest close.
4. Save to `invest/research/<TICKER>-YYYY-MM-DD.md`, then show it.

## Shape

```
# <Company> (<TICKER>): first read, <Weekday, date>

**In one line:** <what it is and the single most important fact about it>

## What it does and how it makes money
- <3 or 4 bullets: products, customers, where the revenue comes from, by segment if reported>

## The record
| | <3 years ago> | <2 years ago> | <last year> | Latest quarter vs a year ago |
| Revenue | | | | |
| Operating margin | | | | |
| Net income | | | | |
| Diluted EPS | | | | |
| Operating cash flow | | | | |
| Long-term debt | | | | |
| Diluted shares | | | | |

## What is going for it
## What is against it
- <from Risk Factors and the numbers: the ones specific to this company, not boilerplate>

## Price today
- <close, date, site>. Price against the last year of earnings (computed).

## What would have to be true
- For this to work out: <2 or 3 conditions>
- For this to go wrong: <2 or 3 conditions>

## Questions worth answering before deciding anything
- <3 open questions and where the answer would be found>
```

- For a comparison, make one table with a column per company and keep to the same rows.
- Offer to add the company to the watchlist. Add it only on a yes.
- No rating, no price target, no buy or sell.

## House rules (every answer)

- Answer first in one or two lines, then short bullets. No long paragraphs.
- Every number names its source and its date: the filing and period, or the site and the day.
- If you could not find something, say "not found". Never estimate a reported number.
- Say plainly when data is a day old, delayed or derived.
- Read-only. Never log in to a brokerage, never place or prepare a trade, never say buy, sell or hold. Lay out the facts and what would have to be true; the decision is the reader's.
- Write dates with the day of the week. Check today's date before you write it.
- Read `invest/lessons.md` in the Homebase folder before you start and follow it. When the reader corrects you or states a preference, add one line to it.
