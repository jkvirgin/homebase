# Working in homebase

## Who you're working with

The person asking for changes is usually not a developer. Use plain language, skip jargon, and when they have to do something themselves, give exact click-by-click steps.

## Do the developer work yourself

Handle the whole Git and GitHub workflow so nobody has to keep track of it afterwards:

- Make each change on its own branch off an up-to-date `main`.
- Commit with a clear message, push, and open a pull request against `main`.
- Merge only when asked. After merging, delete the branch on GitHub and locally, switch back to `main`, and pull.
- Never leave work half-done. End by saying plainly where things stand: merged, or waiting in an open pull request (with its link).

## Keep their plugins current, without being asked

The person does not know plugin commands and should never have to type one. Whenever you start working here, and whenever they say "get the latest", "update", or ask about a skill they do not seem to have:

1. If `main` is clean, run `git pull` so this folder is current.
2. Run `claude plugin marketplace update homebase`. If there is no marketplace called homebase yet, run `claude plugin marketplace add jkvirgin/homebase` first.
3. Run `claude plugin list --json --available`.
4. For every Homebase plugin that is installed, run `claude plugin update <name>@homebase`.
5. If the marketplace has Homebase plugins that are not installed, say what each one does in one plain line and ask which they want. Install the ones they choose with `claude plugin install <name>@homebase`.
6. Tell them in plain words what changed and the first thing to say to try anything new. If anything was installed or updated, say: "Start a new chat for this to take effect."

Do this quietly when nothing has changed; one line is enough. Never remove a plugin unless they ask for it by name. The `update` skill in the memory plugin holds the same steps for chats outside this folder.

## What's here

- `.claude-plugin/marketplace.json` lists the plugins.
- `plugins/invest/`, `plugins/journal/`, `plugins/memory/`, `plugins/trainer/` and `plugins/learn/`, each with a `.claude-plugin/plugin.json` and skills under `skills/<name>/SKILL.md`.
- Three small Python scripts, standard library only, are the only code besides the memory hook: `plugins/invest/skills/sec-data/scripts/edgar.py` (SEC filings and prices), `plugins/trainer/skills/log/scripts/trainer.py` (the training logbook) and `plugins/learn/skills/video/scripts/yt.py` (YouTube transcripts and the notes page). Everything else is skill instructions.
- Scripts never need anything installed. If one needs a package that is not part of Python itself, find another way.

## Rules for changes

- Nothing personal ever goes in this repo: no watchlists, holdings, journal text, health or training data, names or email addresses. Those live only in each person's own Homebase or Journal folder.
- Keep skills short and plain-spoken, in the same voice as the existing ones.
- Suggested folders stay out of Documents and Desktop (`~/Homebase`, `~/Journal`), because those often sync to iCloud.
- When you add a plugin, add it to `.claude-plugin/marketplace.json` and the README, and check that the `update` skill's examples still make sense.
- When invest changes in a way a user would notice, add a line to `plugins/invest/skills/whats-new/CHANGELOG.md` under today's date.
- Update `README.md` when what people install, say or see changes.
