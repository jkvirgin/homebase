#!/bin/sh
# Print the reader's key facts at the start of a chat, so Claude starts with them.
# Reads only ~/Homebase/memory/facts.md. Prints nothing and exits cleanly if it is missing.

dir="$HOME/Homebase/memory"
facts="$dir/facts.md"

[ -f "$facts" ] || exit 0

echo "The reader's saved memory, from $facts (their own file; follow it, and use the remember skill to change it):"
echo
# Keep it short: Claude Code reads at most 10,000 characters from this, so stop well before that.
head -n 200 "$facts" | head -c 8000

if [ -f "$dir/history.md" ]; then
  echo
  echo "A dated history of past work is in $dir/history.md. It is not loaded here; search it with the history skill when the reader asks what was done or decided before."
fi

exit 0
