# Homebase

Small, plain-spoken skills for Claude, for home use. Install what you want; skip the rest.

| Plugin | What it does |
|---|---|
| **invest** | A weekly brief on the companies you follow, quarterly report analysis straight from SEC filings, a view of your own holdings, and first-read research on a company. Read-only: it never logs in to a brokerage and never tells you to buy or sell. |
| **journal** | A private journal. You talk or type, it tidies lightly, and saves a dated file on your own computer. |
| **trainer** | A personal trainer. Tell it what you did, ate, weighed or felt and it keeps the log, plans today's session from your own history and limits, and gives a weekly check-in. Plain files in `~/Homebase/trainer`. |
| **learn** | Paste a YouTube link and get a short TL;DR plus bullet points with clickable timestamps, saved as a page that opens in your browser. It can also suggest videos for what you are learning. |
| **memory** | So you don't have to repeat yourself. Key facts and preferences are read at the start of every chat, and a dated history of what you did and decided can be searched later. Both are plain files in `~/Homebase/memory`. |

## Get started (about ten minutes)

You need a Claude Pro subscription and Claude Code (the Code tab in the Claude desktop app, or the terminal).

**In Claude Code:**

1. Type `/plugin marketplace add jkvirgin/homebase`.
2. Type `/plugin install invest@homebase`. Do the same for any of `journal`, `memory`, `trainer` and `learn`.
3. Type `/plugin`, open the Marketplaces tab, choose homebase and turn on auto-update so you get improvements.
4. Start a new chat and say **"set up invest"** or **"set up my trainer"**.

**In Cowork, if your plan has it:**

1. Open the Claude app and go to **Cowork**.
2. Open **Customize**, then **Plugins**, then **Add marketplace**. Enter `jkvirgin/homebase`.
3. Under **Discover**, install the plugins you want.
4. On the homebase marketplace, turn on **Sync automatically** so you get improvements.
5. Start a chat and say **"set up invest"**. It will ask which companies you follow and make a Homebase folder in your home folder. It suggests your home folder rather than Documents because Documents often syncs to iCloud.

## What to say

- "My weekly brief"
- "Analyze Apple's latest quarter"
- "How is my portfolio" or "I bought 20 Microsoft at 410"
- "Research Costco"
- "Journal entry" and then just talk
- "What's new" to see what changed
- "Set up my trainer", "Log my workout", "I had eggs and toast", "What should I do today", "How was my week"
- Paste a YouTube link, or "Find me a video on pruning apple trees"
- "Update homebase" or "Is there anything new" to get the latest and install new plugins, with Claude doing the steps
- "Remember that…", "What do you remember about me", "Forget that…"
- "Log this", "What did we do about…", "When did we…"

## Your data is yours

- Your watchlist, holdings, journal, memory, training log and video notes are ordinary files on your own computer. Nothing personal is ever stored in this repository or sent to whoever maintains it.
- Numbers come from SEC EDGAR, the government's free filing system. Prices are end-of-day closes from public quote pages, and news comes from web search; both can be delayed.
- Anything you type to Claude is sent to Anthropic, as with any chat. Say "is my journal private" for the plain version.
- Video transcripts are read from YouTube the way its own app reads them. That is unofficial and can stop working; only the video's address is sent.
- This is information to help you read your own investments. It is not financial, tax or legal advice.
- The trainer is a coach, not a doctor. It follows the limits you give it and is not medical advice.

## If something is off

Ask Claude first: "that number looks wrong, check it against the filing" works. To get the latest version in Claude Code, say "update homebase" and Claude runs the steps for you (or type `/plugin marketplace update homebase` yourself). In Cowork, open Customize, Plugins, the homebase marketplace, and select **Check for updates**.
