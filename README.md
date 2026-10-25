# Terminal Comfort Guide

A friend-style command-line manual for total beginners — the calm gateway to
local AI. Plain English, step by step, never condescending.

Written in the spirit of
[Dylan Asdale's *The Massive AI Manual*](https://dylanasdale.github.io)
and published as an open-source project by **Asdale Dynamics, LLC**.

## What you get

- **`docs/`** — the entire manual in readable Markdown:
  - Welcome + 10 chapters: opening a terminal (Windows/mac/Linux), moving
    around folders, safe copy-paste, what a command is, running Ollama
    (local AI) calmly, using pip, reading error messages, admin & sudo,
    your first tiny script, and where to go next.
  - **10 practice exercises + a full answer key** (with reasoning).
  - A **glossary** of every term used, and a **fear-reducing FAQ**.
- **`engine/build.py`** — a zero-dependency build script (Python 3 standard
  library only) that converts the Markdown into a polished static HTML site
  in `site/`.
- **`scripts/hello_local_ai.py`** — the friendly "first tiny script" from
  Chapter 9, ready to run and used by the test suite.
- **`tests/`** — a standard-library (`unittest`) test suite covering the
  Markdown converter, the built site, internal links, and the hello script.

No installs, no accounts, no network required to build or read anything
local-first. Nothing in this project collects or transmits data.

## Run it

Requires Python 3 (any recent version; nothing else).

Build the site:

```
python3 engine/build.py
```

Then open **`site/index.html`** in any browser — or double-click it, no
server needed.

Verify links without leaving build output behind:

```
python3 engine/build.py --check
```

Run the example script:

```
python3 scripts/hello_local_ai.py        # Mac / Linux
py scripts/hello_local_ai.py             # Windows
```

Run the tests:

```
python3 -m unittest discover -s tests -v
```

## Project layout

```
docs/      the manual (Markdown, one file per chapter)
engine/    build script (Markdown -> HTML, stdlib only)
scripts/   first-script example
site/      built output (generated; not committed)
tests/     unittest suite
```

## License

MIT — see [LICENSE](LICENSE).

Copyright (c) 2026 Asdale Dynamics, LLC
