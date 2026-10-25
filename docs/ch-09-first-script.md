# Chapter 9 — Your First Tiny Script (Written by You, Finally)

Nine chapters in, and here's my favorite part. You're going to write a
program with your own hands, in a text editor you already have, run it in
your terminal, understand every single line of it — and then improve it
yourself. No frameworks, no AI needed, nothing to install.

## What a "script" actually is

A script is just a **file full of instructions, saved with a name**, that
the terminal can run whenever you ask. Compare:

- A *command* is one sentence ("please list my files").
- A *script* is a paragraph ("please do these six things in order").

That's honestly the entire difference. You've been writing sentences for
nine chapters; scripts are paragraphs.

## Step 1 — Make a practice folder (Chapter 2 skills)

Open your terminal and:

```
cd
mkdir terminal-practice
cd terminal-practice
pwd
```

`mkdir` = **m**a**k**e **d**irectory. That's your first *change* command in
this manual and it's the gentlest one possible: it creates one empty folder
in your home area. `pwd` should show you standing inside
`.../terminal-practice`. From now on, *this folder is your lab*, and
everything we make together lives here.

## Step 2 — Open the file in your editor

Every operating system ships with a plain-text editor, and any of these will
do for a first script:

- Windows: open **Notepad** (Windows key, type `notepad`), then **File →
  Save As** into your `terminal-practice` folder.
- Mac: TextEdit is installed, but you must convert it first: **Format →
  Make Plain Text** (⇧⌘T) — *this one step matters*, because rich-text
  Mac editors sneak formatted text into your script. Or use VS Code if you
  have it (later it's the best; today, Notepad/TextEdit is fine).
- Linux: whatever your distro calls its text editor is fine (gedit,
  Kate, or plain nano in the terminal).

(You may also hear of the terminal editors `nano` and `vim`. Resist `vim`
for now — it has famous jokes about beginners being trapped in it. `nano`
is fine and honest if you want an in-terminal editor: type `nano hello.py`
to open it.)

Save the (empty for now) file as:

```
hello.py
```

The `.py` ending is Python's way of saying "I contain Python instructions."
The period-and-letters ending is called the **file extension** — it's for
the programs, not for decoration.

## Step 3 — Type these five lines

Into your new file, type exactly:

```python
# my first script - says hello, tells the time, counts my folders

import os
from datetime import datetime

print("Hello! This is my first script.")
print("The time right now is:", datetime.now())
print("Here is what's in", os.getcwd(), ":")
for thing in sorted(os.listdir(".")):
    print("  -", thing)
```

Now — before you run it — let's read every line together, because
**understanding it is the whole graduation**, and this script is genuinely
the gateway to *all* of your future AI tools:

1. `"# my first script..."` — a **comment**. Python ignores lines starting
   with `#`. They're notes to humans, like margin notes in your book.
2. `import os` — "load my toolbox about the **o**perating **s**ystem" (the
   one that knows about folders and files).
3. `from datetime import datetime` — "from my toolbox about time, hand me
   the `datetime` tool."
4. `print(...)` — show text on the screen. You already know `print`'s
   cousin from shell commands; Python's version is the same personality.
5. `os.getcwd()` = "get current working directory" — *your `pwd` command*
   from Chapter 2, now as a Python function. Same idea, same house.
6. `for thing in sorted(os.listdir(".")):` — "for each item in the list of
   things in this folder (`.` — 'this folder' — also from Chapter 2!),
   sorted alphabetically, do the next indented line."

See what happened there, deeper than any tutorial tells you: **your shell
commands and Python code share concepts.** `pwd` ↔ `os.getcwd()`.
`ls` ↔ `os.listdir()`. "This folder" `.` ↔ `"."`. You're not learning two
worlds; you're learning one world in two dialects. You already know more
than you feel like you know.

Save the file. (Ctrl+S / Cmd+S. Do it now; do it every time. Forgetting to
save is the single most common beginner error in existence, and Chapter 7's
rule #4 covers it.)

## Step 4 — Run it

Back in your terminal, still inside your practice folder:

```
pwd
```

(confirm you're in `terminal-practice`), then:

- Mac/Linux: `python3 hello.py`
- Windows: `py hello.py`

Expected output, more or less:

```
Hello! This is my first script.
The time right now is: 2026-10-25 09:14:33.123456
Here is what's in /Users/you/terminal-practice :
  - hello.py
```

**You wrote a program.** That list of files at the bottom is *your computer
reporting to you*, from code *you* typed. It will list `hello.py` itself,
because the script is asking about its own folder. (If you saved the file
into a different folder than the one you're standing in — very common and
completely fine — Chapter 7 rule #2 now applies: `cd` to where the file
actually is, or run `py full/path/to/hello.py`.)

## Step 5 — Make it yours (the actual fun)

Change `print("Hello! This is my first script.")` to say anything you like —
your dog's name, your coffee order. Save, run again. Change `"."` to `".."`
(spot the Chapter 2 callback: two dots = the folder upstairs) and run again
— now it lists what's in your home folder instead.

Then try this one: what happens if you make a typo, like
`print("Hello!)` (missing the closing quote) and run it? **Don't avoid the
error — run straight at it.** Read the last line first, find the part
Python points at with the little arrow, fix it, run again. That loop —
write, run, read, fix, run — is *the entire job* in miniature, and you just
did it on day one.

## What's in this repo, to prove it works

Inside this very project you downloaded, there's a finished, slightly
fancier version of this exact idea at `scripts/hello_local_ai.py` — a
friendly script that greets you, shows Python's version, counts the files
in the current folder, and prints a local-first AI motivation at the end.
Run it after Chapter 9 as a sent-yourself-a-certificate moment:

```
python3 scripts/hello_local_ai.py
```

(From the top level of this downloaded project folder. This project's own
tests run that script automatically, so "it works" is checked, not
promised.)

Next and last stop, friends: [Chapter 10](ch-10-where-next.html) — where
this path leads, and how to keep the momentum without burning out.
