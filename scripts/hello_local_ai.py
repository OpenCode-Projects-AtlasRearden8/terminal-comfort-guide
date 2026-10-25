#!/usr/bin/env python3
"""hello_local_ai.py — the friendly first script from Chapter 9.

Run it from anywhere:

    python3 scripts/hello_local_ai.py        (Mac / Linux)
    py scripts/hello_local_ai.py             (Windows)

It does nothing risky: it greets you, shows Python's version, counts the
files in the folder it is run from, and waves you toward local AI.
SQLite-grade unexciting, on purpose. Local-first: no network is touched.
"""

from datetime import date
import os
import platform
import sys

BANNER = r"""
 _   _      _            _             _ _   _
| | | | ___| | __      | |        ___| (_) | (_)_ __   ___ _ __
| |_| |/ _ \ |/  __  | |       / _ \ | | | | | '_ \ / _ \ '__|
|  _ /|  __/   <    /\| |/\__  | (_) / | | | | | | ||  __/ |
|_| |_|\___|_|\_\ \/  \/   /   \___/|_|_|_|_|_| |_|(_\___|_|
"""


def main() -> int:
    now = date.today().strftime("%A, %B %d, %Y")
    python_version = platform.python_version()
    here = os.getcwd()
    try:
        entries = sorted(os.listdir(here))
    except OSError as exc:
        print(f"I could not read the folder ({exc}); still greeting you though.")
        entries = []

    print(BANNER)
    print("Hello! This is your first script, running successfully.")
    print(f"Today is: {now}")
    print(f"Python version is: {python_version}")
    print(f"You are standing in: {here}")
    print(f"There are {len(entries)} item(s) in this folder:")
    for name in entries:
        marker = "/" if os.path.isdir(os.path.join(here, name)) else ""
        print(f"  - {name}{marker}")
    print()
    print("Every AI tool you'll ever meet starts from moves exactly like these:")
    print("install once, list what you have, run a named thing, read the output.")
    print("You just did two of them. Keep the pace, friend.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
