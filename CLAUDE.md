# Working in homebase

## Who you're working with

The person asking for changes is usually not a developer. Use plain language, skip jargon, and when they have to do something themselves, give exact click-by-click steps.

## Do the developer work yourself

Handle the whole Git and GitHub workflow so nobody has to keep track of it afterwards:

- Make each change on its own branch off an up-to-date `main`.
- Commit with a clear message, push, and open a pull request against `main`.
- Merge only when asked. After merging, delete the branch on GitHub and locally, switch back to `main`, and pull.
- Never leave work half-done. End by saying plainly where things stand: merged, or waiting in an open pull request (with its link).

## What's here

- `.claude-plugin/marketplace.json` lists the plugins.
- `plugins/invest/` and `plugins/journal/`, each with a `.claude-plugin/plugin.json` and skills under `skills/<name>/SKILL.md`.
- `plugins/invest/skills/sec-data/scripts/edgar.py` is the only code; everything else is skill instructions.

## Rules for changes

- Nothing personal ever goes in this repo: no watchlists, holdings, journal text, names or email addresses. Those live only in each person's own Homebase or Journal folder.
- Keep skills short and plain-spoken, in the same voice as the existing ones.
- Suggested folders stay out of Documents and Desktop (`~/Homebase`, `~/Journal`), because those often sync to iCloud.
- When invest changes in a way a user would notice, add a line to `plugins/invest/skills/whats-new/CHANGELOG.md` under today's date.
- Update `README.md` when what people install, say or see changes.
