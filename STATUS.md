# STATUS

**Project:** Terminal Comfort Guide — a friend-style command-line manual for
total beginners, serving as the calm gateway to local AI.
**Owner/publisher:** Asdale Dynamics, LLC (Dylan Asdale).
**Date:** 2026-10-25
**Status:** complete, tested, building cleanly. Local-first; nothing in the
project requires network access beyond one-time optional downloads described
*inside* the manual (Ollama, Python, pip packages).

## What was built

### The manual (docs/, 15 Markdown documents)

- `00-welcome.md` — promise-setting intro: what the manual will/won't do,
  what "local-first" means, a chapter roadmap table.
- `ch-01-open-a-terminal.md` — opening a terminal on Windows (Terminal app /
  PowerShell), macOS (⌘Space), Linux (all desktop families), first command
  (`echo`), safe quitting.
- `ch-02-moving-around.md` — `pwd`, `ls`/`dir`, `cd`, `.`/`..`, bare-`cd`
  home shortcut, absolute vs relative paths, `~`, a guided walk homework.
- `ch-03-safe-copy-paste.md` — the "gray-box rule", clipboard-hijack
  awareness, per-OS paste keys, the paste-pause-enter ritual, `sudo`/
  admin-paste caution, the 90%-of-terminal-safety sentence.
- `ch-04-running-things.md` — command grammar (name + arguments + flags),
  what PATH is (conceptually), `--help`, read-only vs changing commands,
  respect rules for `rm`, intro to tab completion.
- `ch-05-ollama.md` — local-first AI: installing Ollama (Windows/mac/Linux),
  verifying with `--version`, model sizing guidance, `ollama run
  llama3.2:1b`, the six-command survival kit, and why local matters.
- `ch-06-pip.md` — checking Python/pip (`python3 -m pip`), a gentle first
  install (`emoji`), the pip survival kit, verification one-liner, and two
  beginner rules (install carefully; "already satisfied" ≠ error).
- `ch-07-reading-errors.md` — four reading rules, the Big Five beginner
  errors decoded (`command not found`, `No such file or directory`,
  `Permission denied`, `ModuleNotFoundError`, `SyntaxError`), a 20-second
  error routine.
- `ch-08-admin-and-sudo.md` — user-zone vs admin-zone mental model, what
  sudo really is, hidden-password behavior, three green lights + one red
  light for admin use, calm homework (`sudo -v` / `sudo -k`).
- `ch-09-first-script.md` — a practice folder, a five-line Python script
  written and understood line by line, running it, improving it, and
  deliberately meeting a first error.
- `ch-10-where-next.md` — onward path (models, life-scripts, git, local AI
  utilities, only-then-cloud), three habits, pacing advice for busy adults,
  and three carry-everywhere questions.
- `ch-11-exercises.md` — 10 exercises + a bonus, strictly drawn from
  Chapters 1–9, nothing destructive.
- `ch-12-answer-key.md` — every answer with the reasoning (not just the
  answer), including common gotchas.
- `glossary.md` — ~35 terms, one plain definition each.
- `faq.md` — fear-reducing FAQ ("am I going to break something?", hidden
  sudo password, Ctrl+C, output mismatch, offline use, etc.).

### Static site

- `engine/build.py` — zero-dependency (Python 3 stdlib only) build script
  converting the Markdown into a styled static HTML site with sidebar TOC,
  prev/next navigation, and a per-page LLC credit footer. Supports headings,
  fenced code, inline code/bold/italic, links, bullet & ordered lists,
  blockquotes, tables, and horizontal rules. Subcommands: default build to
  `site/`, `--out DIR`, and `--check` (build to temp, verify links only).
- `site/` — generated output (15 pages), gitignored; rebuilt in <1 second.

### Content / community

- `scripts/hello_local_ai.py` — the friendly first script (greeting, date,
  Python version, folder listing, local-AI encouragement). No network.
- `tests/test_build.py` — 22 tests: converter unit tests, full-site build
  tests (every page built, no broken internal links, LLC credit present on
  every page, exercises count, glossary size), and subprocess tests of the
  hello script and the `--check` build mode.
- `README.md` — project intro, LLC credit, how to run everything.
- `LICENSE` — MIT, copyright line exactly "Copyright (c) 2026 Asdale
  Dynamics, LLC".
- `.gitignore` — `site/`, `__pycache__/`, OS junk.

## How to run it

All commands from the project root and from **Python 3 standard library
only** (no installs needed):

```bash
python3 engine/build.py                        # build the site -> site/
python3 scripts/hello_local_ai.py              # the first-script example ("py" on Windows)
python3 -m unittest discover -s tests -v       # run the test suite
python3 engine/build.py --check                # link-check only, no artifacts
```

Read the built site by opening `site/index.html` in any browser (no server
needed), or read `docs/*.md` directly. Safe copy-paste warning examples are
only prose; nothing here runs Ollama/pyPI access itself.

## Verification results (all run locally)

- `python3 engine/build.py` — builds **15 pages**, reports `OK: 15 pages
  built, all internal links resolve.` RC 0.
- `python3 engine/build.py --check` — same result in a temp dir, no residue.
- `python3 -m unittest discover -s tests` — **22/22 tests passed** (RC 0),
  covering the converter, built-site integrity, internal links, LLC credit
  on every page, the hello script, and the check mode.
- `python3 scripts/hello_local_ai.py` — runs cleanly, prints greeting,
  date, Python version, folder listing; RC 0.
- Grep sweep over generated HTML found no unrendered Markdown artifacts
  (stray `**`, leftover heading `#`, raw `|` table rows).
- Known parser cases are pinned by unit tests: ordered-list item splitting,
  soft-wrap paragraph joining, bold spanning wrapped lines, table separator
  row handling, HTML escaping in prose and code blocks.

## Known gaps (honest list)

- The Markdown converter is intentionally small; exotic Markdown (nested
  lists, footnote syntax, images, HTML comments) is *unsupported* rather
  than broken — none of the shipped content uses it.
- Terminal screenshots/illustrations: none (text-only by design; screenshots
  would need to be produced per-OS and could go stale).
- Ollama chapter documents the *current* model name `llama3.2:1b`; model
  names evolve, so a future edition may need a one-line update.
- No dark/light theme toggle (single calm paper-like theme).
- No search box; readers navigate via sidebar/glossary (fine at this size).
- Tests are stdlib `unittest`; a pytest migration would be nice later and is
  easy (same assertions).
- The site is plain static HTML; a hosted version (GitHub Pages) is a
  natural next step but was deliberately NOT done (no publishing performed).

## Privacy & safety notes

- No secrets, API keys, or personal data anywhere in the repository.
- No telemetry, no external fonts, no CDN assets; the site is fully
  self-contained and works offline.
- Git was initialized locally only; committed with the repo's existing
  identity; never pushed, no remote configured, nothing published.

— Generated as part of the ASDALE DYNAMICS, LLC local-first beginner series.
