#!/usr/bin/env bash
set -euo pipefail

WATCH_DIR="/mnt/c/Users/rexch/Downloads"
SORTER="/home/seraph/folder_sort/main.py"
LOCK="/tmp/folder_sort.lock"

echo "Polling $WATCH_DIR every min… (Ctrl-C to stop)"

while true; do
  # prevent overlap if a previous run is slow
  if flock -n "$LOCK" -c "python3 \"$SORTER\" --dir \"$WATCH_DIR\""; then
    :
  else
    echo "Sorter already running, skipping this tick"
  fi
  sleep 60
done
