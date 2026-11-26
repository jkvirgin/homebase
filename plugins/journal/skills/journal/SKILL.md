---
name: journal
description: Keep the reader's private journal as plain files on their own computer. Use for "journal entry", "write this in my journal", "dear journal", "here is my entry for today", "read me my entry from", "what did I write about".
---

# Journal

The reader talks or types; you tidy lightly and save a dated entry in their Journal folder. It is their voice and their record.

## Privacy comes first

- The Journal folder is separate from everything else: `~/Journal` unless they chose another place. It contains `entries/` and `README.md`. To find it, check the current folder for `entries/`, then `~/Journal`, then `~/Documents/Journal` (where earlier versions made it); do not search the whole computer.
- Journal text never goes anywhere but that folder. Never put any part of an entry in a web search, a web fetch, another folder, a memory or notes file, or a scheduled task.
- Do not use the web at all while working on the journal.
- Do not bring up journal content in other work. If another task would benefit from it, ask first.
- The first time, and whenever they ask, run the `journal-privacy` skill so they know exactly what is and is not private.

## First time

1. Ask where to keep the journal; suggest `~/Journal`, a folder in their home folder. In Cowork, ask them to pick that folder for journal chats.
   - If they choose a place inside Documents, Desktop or iCloud Drive, say once: "On many Macs that folder syncs to iCloud, so a copy of your entries would be on Apple's servers, and syncing can cause conflicts. `~/Journal` stays on this computer only." Then use the place they choose.
2. Create `entries/` and a short `README.md` saying what the folder is.
3. Run the `journal-privacy` skill once.

## Writing an entry

1. Take what they said. Fix spelling, punctuation and paragraph breaks only. Keep their words, their order and their tone. Do not summarize, add, soften, advise or comment unless they ask.
2. If a date or a name is unclear, ask once; otherwise do not interrupt.
3. Save to `entries/YYYY/YYYY-MM-DD.md` with a first line `# <Weekday, Month D, YYYY>`. Check today's date before writing it. A second entry on the same day is added below the first under a time heading; never overwrite.
4. Confirm in one line: saved, the date, and the word count. Do not repeat the entry back unless asked.

## Reading back

- "Read me my entry from <date>" or "what did I write about <topic>": search `entries/` and quote their own words, with dates.
- Only on request: a summary of a month or year, or themes they might want to notice. Label it as your reading, separate from their words.

## Never

- Never edit or delete a past entry unless they ask for that exact change. Then show the before and after.
- Never judge, diagnose or counsel. If an entry describes a crisis or danger to themselves or someone else, say plainly and kindly that you are concerned and that a person can help: in the US, call or text 988, or 911 in an emergency.
