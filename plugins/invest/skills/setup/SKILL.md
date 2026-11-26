---
name: setup
description: First-time setup for the invest skills, or a repair of the Homebase folder. Use when the reader says "set up", "get started", "add a stock to my watchlist", "change my watchlist", or when another invest skill finds no Homebase folder.
---

# Setup

Create the reader's Homebase folder and fill it in with them. Everything personal lives in this folder on their computer. Nothing personal is ever written anywhere else.

## Find or make the folder

1. Look for a folder that contains `invest/watchlist.md`: the current working folder first, then `~/Documents/Homebase`. Check those two places only; do not search the whole computer.
2. If there is none, ask where to make it and suggest `~/Documents/Homebase`. In Cowork, ask them to pick that folder for this chat.
3. Create only what is missing. Never overwrite a file that exists.

```
Homebase/
  CLAUDE.md             house rules and where things are
  invest/
    watchlist.md        companies to follow
    holdings.csv        what they own (optional)
    settings.md         contact email for SEC, preferences
    lessons.md          corrections and preferences, one per line
    briefs/             weekly briefs, one file per date
    reports/            quarterly report analyses
    research/           notes on companies they are considering
    filings/            saved filing text (safe to delete)
```

## Ask, one question at a time

1. **Which companies do you want to follow?** Take names or tickers. Confirm each ticker and company name back before saving. Write `invest/watchlist.md` as a table: Ticker, Company, Why I follow it, Added (date).
2. **Do you want to track what you own?** If yes, hand off to the `portfolio` skill. If no, skip; they can add it any time.
3. **An email address for the SEC.** Explain it in these words: "The SEC's free data service asks every program to give a contact email. Yours would be sent to sec.gov only, and stored only in your own settings file." Save it in `invest/settings.md` as `sec_contact: <email>`. If they would rather not, save `sec_contact: none`; the skills then read filings through web pages, which is slower and less complete.
4. **How do you like your brief?** Short or detailed, and which day of the week. Save in `invest/settings.md`.

## Write CLAUDE.md in the Homebase folder

Write the house rules below into `CLAUDE.md`, plus one line each on where the watchlist, holdings, settings and lessons files are.

## House rules (every answer)

- Answer first in one or two lines, then short bullets. No long paragraphs.
- Every number names its source and its date: the filing and period, or the site and the day.
- If you could not find something, say "not found". Never estimate a reported number.
- Say plainly when data is a day old, delayed or derived.
- Read-only. Never log in to a brokerage, never place or prepare a trade, never say buy, sell or hold. Lay out the facts and what would have to be true; the decision is the reader's.
- Write dates with the day of the week. Check today's date before you write it.
- Read `invest/lessons.md` in the Homebase folder before you start and follow it. When the reader corrects you or states a preference, add one line to it.

## Finish

- Read the watchlist back in one short table.
- Tell them the four things they can now ask for: "my weekly brief", "analyze <company>'s latest quarter", "how is my portfolio", "research <company>".
- Offer a weekly schedule for the brief. A scheduled brief needs their folder, so it runs when their computer and the Claude app are on.
