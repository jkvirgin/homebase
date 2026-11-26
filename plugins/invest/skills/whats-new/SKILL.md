---
name: whats-new
description: Explain what the invest skills can do and what changed recently. Use for "what's new", "what can you do with my stocks", "help with invest", "which version do I have", "did I get the update".
---

# What's new and what this does

1. Read [CHANGELOG.md](CHANGELOG.md) and tell the reader the newest entry and its date in two or three plain lines. That date is their version.
2. List what they can ask for:
   - "my weekly brief"
   - "analyze <company>'s latest quarter"
   - "how is my portfolio" and "I bought / I sold ..."
   - "research <company>"
   - "add <company> to my watchlist"
3. If they expected something newer, or ask whether there is anything new: in Claude Code, do it for them. Run `claude plugin marketplace update homebase`, then `claude plugin update invest@homebase`, then `claude plugin list --json --available` to see whether Homebase has plugins they have not installed, and offer those. Tell them to start a new chat afterwards. In Cowork, where you cannot run commands, give the steps: open Customize, then Plugins, choose the homebase marketplace and select Check for updates.

Keep it short. Do not explain how plugins work unless asked.
