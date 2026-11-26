---
name: update
description: Get the newest Homebase skills and install any new plugins, doing every step for the reader. Use for "update homebase", "get the latest", "update my skills", "are there new plugins", "install the new skills", "install the trainer", "install learn", "is there anything new", "I was told there's an update", or when the reader asks for something a Homebase plugin does that is not installed yet.
---

# Update Homebase

The reader is not a developer and should never have to type a plugin command. Run every step yourself and tell them the result in plain words.

## Steps

1. Refresh the list of what is available:

```
claude plugin marketplace update homebase
```

   If it says there is no marketplace called homebase, add it first with `claude plugin marketplace add jkvirgin/homebase`, then carry on.

2. See what is installed and what is available:

```
claude plugin list --json --available
```

3. Update every Homebase plugin that is installed. For each one:

```
claude plugin update <name>@homebase
```

4. Find Homebase plugins that are available but not installed. Tell the reader what each one does in one plain line (use its description) and ask which they want. If they already asked for a particular one, skip the question. Install each one they choose:

```
claude plugin install <name>@homebase
```

5. Finish in a few lines:
   - what was updated, and what is new in it if a changelog says;
   - what was installed, and the first thing to say to try it ("set up my trainer", or paste a YouTube link);
   - **"Start a new chat for this to take effect."** New and updated skills load when a chat starts. Say this every time something changed.
   - If nothing changed, say "You already have the latest."

## So this happens without asking, once

After the first successful update, check whether updates are set to arrive automatically. If you cannot tell, give these steps once and offer to walk through them:

1. Type `/plugin` and press Return.
2. Go to the **Marketplaces** tab.
3. Choose **homebase**.
4. Turn on **auto-update**.

Do not repeat these steps in later chats unless they ask.

## Rules

- These commands only fetch from the public Homebase repository and change which plugins are installed. They never touch the reader's own files in `~/Homebase` or `~/Journal`.
- Install only plugins from the `homebase` marketplace here. If they ask for something from anywhere else, that is a separate decision; say so and ask.
- Never remove a plugin unless they ask for that plugin by name.
- If a command fails, show the one line that says why, try once more, then stop and say plainly what did not work. Do not edit Claude's settings files by hand to force it.
