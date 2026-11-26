---
name: history
description: Keep a dated history of what the reader and Claude did and decided, and look things up in it later. Use for "log this", "save what we did", "add this to the history", "what did we do about", "when did we", "have we done this before", "remind me what we decided", "what happened last time".
---

# History

A dated log in `~/Homebase/memory/history.md` on the reader's own computer. Unlike `facts.md`, it is not read at the start of every chat; search it when you need it.

## The file

If it does not exist, create it (the `remember` skill describes the folder):

```
# History

Newest first. One heading per day.
```

Each day is a heading `## <Weekday, Month D, YYYY>`, newest at the top. Under it, one line per thing done or decided: what happened and where, with links or names that make it findable later. For example:
`- Moved homebase's suggested folders out of Documents (iCloud). Merged as pull request jkvirgin/homebase#1.`

## Logging

- When the reader says "log this" or "save what we did", add the day's lines. Check today's date first. Add to today's heading if it exists; never rewrite older days.
- At the end of real work (something built, changed, decided or set up), offer once: "Should I add today's work to your history?" Do not offer after a quick question.
- Write outcomes, not chatter: what changed, what was decided and why, what is still open.
- The same "never save" rules as `remember` apply: no passwords or account numbers, nothing from the journal.

## Looking things up

- "What did we do about …", "when did we …": search `history.md` for the words and close variants. Answer in one or two lines with the date, then quote the matching lines.
- If nothing matches, say "not found in your history" and do not guess.
- If the answer is a lasting fact or preference, offer to add it to `facts.md` with the `remember` skill.
