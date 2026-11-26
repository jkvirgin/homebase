---
name: journal-privacy
description: Explain plainly what is and is not private about the journal, and the one setting to check. Use for "is my journal private", "who can see my journal", "does Anthropic read this", "journal privacy", and once during first-time journal setup.
---

# What is private, in plain words

Say this in your own short words. Do not soften it and do not oversell it.

**What stays on your computer**
- Your entries are ordinary files in your Journal folder. They are not in any app's database and not in the plugin. You can read them without Claude, back them up, or delete them.
- One exception: if the folder is inside Documents, Desktop or iCloud Drive, a Mac may sync it to iCloud, which puts a copy on Apple's servers. `~/Journal`, the suggested place, does not sync.

**What does not**
- To tidy or search an entry, Claude has to read it. That text is sent to Anthropic, the company that makes Claude, the same as anything else you type to Claude. This skill cannot change that.
- The conversation itself is kept in your Claude chat history until you delete it.

**The one setting to check**
- In the Claude app: Settings, then Privacy, then the model-improvement switch (labelled "Help improve our AI models" at the time of writing). Off means your chats are not used to train models, and Anthropic says it then keeps them for about 30 days, not years.
- Wording and retention can change. Anthropic's current terms are at privacy.claude.com; read that page if this matters to you, and trust it over this note.

**If that is not private enough**
- Write entries yourself, straight into the folder, and never open them with Claude. Use Claude only for the entries you are comfortable sharing with it. Both kinds can live in the same folder.

**What this skill promises**
- It never searches the web with your words, never copies an entry outside the folder, and never runs on a schedule.

After explaining, ask whether they would like help finding the setting. Do not change any setting yourself.
