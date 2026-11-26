# Homebase

Small, plain-spoken skills for Claude, for home use. Install what you want; skip the rest.

| Plugin | What it does |
|---|---|
| **invest** | A weekly brief on the companies you follow, quarterly report analysis straight from SEC filings, a view of your own holdings, and first-read research on a company. Read-only: it never logs in to a brokerage and never tells you to buy or sell. |
| **journal** | A private journal. You talk or type, it tidies lightly, and saves a dated file on your own computer. |

## Get started (about ten minutes)

You need a Claude Pro subscription and the Claude desktop app.

1. Open the Claude app and go to **Cowork**.
2. Open **Customize**, then **Plugins**, then **Add marketplace**. Enter the address of this repository.
3. Under **Discover**, install **invest**, **journal**, or both.
4. On the homebase marketplace, turn on **Sync automatically** so you get improvements.
5. Start a chat and say **"set up invest"**. It will ask which companies you follow and make a Homebase folder in your Documents.

Using Claude Code instead: `/plugin marketplace add <owner>/<repo>`, then `/plugin install invest@homebase`.

## What to say

- "My weekly brief"
- "Analyze Apple's latest quarter"
- "How is my portfolio" or "I bought 20 Microsoft at 410"
- "Research Costco"
- "Journal entry" and then just talk
- "What's new" to see what changed

## Your data is yours

- Your watchlist, holdings and journal are ordinary files on your own computer. Nothing personal is ever stored in this repository or sent to whoever maintains it.
- Numbers come from SEC EDGAR, the government's free filing system. Prices and news come from web search and can be delayed.
- Anything you type to Claude is sent to Anthropic, as with any chat. Say "is my journal private" for the plain version.
- This is information to help you read your own investments. It is not financial, tax or legal advice.

## If something is off

Ask Claude first: "that number looks wrong, check it against the filing" works. To get the latest version, open Customize, Plugins, the homebase marketplace, and select **Check for updates**.
