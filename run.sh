#!/usr/bin/env bash
# Jalankan Video Downloader (macOS / Linux)
cd "$(dirname "$0")"
if [ ! -d .venv ]; then
  python3 -m venv .venv
  .venv/bin/pip install -r requirements.txt
fi
.venv/bin/python app.py
