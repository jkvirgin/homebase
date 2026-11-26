---
name: recommend
description: Suggest YouTube videos for something the reader wants to learn, and keep their learning topics and watch list. Use for "find me a video on", "recommend a video", "what should I watch", "I want to learn about", "add this to my watch list", "what's on my watch list", "what am I learning".
---

# What to watch

Find a few good videos for what the reader is learning, say why each is worth their time, and keep the list.

## The file

`~/Homebase/learn/topics.md` (if the current folder has `learn/`, use that). Create it if missing:

```
# Learning

## Topics
- <topic>: <what they want out of it, their level> (added YYYY-MM-DD)

## To watch
- [Title](https://www.youtube.com/watch?v=...) · Channel · length · why (added YYYY-MM-DD)

## Watched
- [Title](link) · YYYY-MM-DD · notes in videos/<file>
```

## Finding videos

1. Know the topic and their level. If `topics.md` does not say, ask one question: what they already know and what they want to be able to do.
2. Web search for videos on it. Search by topic only; put nothing personal in a search.
3. Check that each candidate is real before suggesting it:

```
python3 ${CLAUDE_PLUGIN_ROOT}/skills/video/scripts/yt.py info "<link>"
```

   If that path shows as literal text, the script is `scripts/yt.py` inside the `video` skill of this plugin. Drop any link it reports as unavailable. Never suggest a link you have not checked, and never make one up.
4. Pick three to five. This reader learns best by seeing, so prefer videos that show the thing: demonstrations, diagrams, animations, worked examples. Prefer the people who do the work over commentary about it, and a 15-minute video that teaches over a 2-hour one that wanders.

## Shape

```
**In one line:** <what these will get them>

1. [Title](link) · Channel · length
   Why: <one line: what it shows and why it suits them>
2. ...

Say "summarize the first one" for the notes before you watch, or "add these to my list".
```

- Say plainly that you have not watched them: the choice is based on title, channel and search results. The `video` skill gives the real picture in a minute.
- Add to "To watch" only on a yes. Move a video to "Watched" when the `video` skill has made notes for it.
- "What's on my list": read it back, newest first, and offer to summarize the top one.
