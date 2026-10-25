# Chapter 12 — Answer Key (with Reasoning, Not Just Answers)

Answers first, reasons always. The reason is the part you take with you.

## Exercise 1 — Orientation

```
pwd
ls
```

*Why these:* `pwd` (print working directory) answers *where am I*; `ls`
(list) answers *what's around me*. These two are the beginner's compass.
Order matters only in your mind: knowing where you are first makes what
you see easier to interpret.

**Gotcha addressed:** nothing happens on screen until Enter — a `pwd` that
"sits there" isn't frozen; it's *listening*. That blinking cursor after
the prompt is patience, not failure.

## Exercise 2 — The teleporter

```
cd
pwd
```

*Why this works:* bare `cd` — no destination — is the "go home" button on
every system we covered. The `pwd` is the verification step; doubling
through `cd ..` several times works, but isn't the *point* of the
exercise: the point is knowing the shortcut exists and works everywhere.

## Exercise 3 — A round trip

```
cd Documents
pwd
cd ..
```

*Why:* walking in is Chapter 2's `cd Documents`; confirming is `pwd`;
`..` means "the folder one level up," i.e., out of Documents and back
into your home area. Three commands, zero risk, and this is the exact
muscle we'll use ten thousand times over a terminal life.

**Gotcha addressed:** if your `cd Documents` failed with a *name* error,
see Exercise 7 — it's the same issue with a different folder.

## Exercise 4 — Make and inspect

```
mkdir my-notes
cd my-notes
mkdir drafts
cd ..
ls
```

*Why:* `mkdir` creates one empty folder. Then walk in, make the nested
one, walk back out, and `ls` to confirm both exist. The compact version
works too:

```
mkdir my-notes/drafts
```

...because a **path** can be part of a command (Chapter 2: slash means
"inside"), so this says "make `drafts` *inside* `my-notes`." But making
that leap is optional today; the long way teaches walking.

**Gotcha addressed:** `my-notes` vs `my_notes` vs `My Notes` are three
different folders to the computer. Any spelling is fine — *your*
spelling, consistently. The skill isn't guessing names; it's
`ls` to look at what you actually named it.

## Exercise 5 — First wave + variable

```
echo I am learning, calmly
```

*Why:* `echo` takes *all* the words after it and repeats them. One echo,
your whole phrase. The comma is just part of the text; `echo` isn't
parsing your sentence, it's repeating it.

**Gotcha addressed:** on the Mac, typing a *quote* never opens or closes
anything by accident — plain `echo` takes it literally. On Windows
PowerShell, commas *can* look like list separators to advanced features
of PowerShell — so if you later use echoes inside scripts, prefer the
quoted form `echo "I am learning, calmly"` to be safe everywhere.

## Exercise 6 — Read-the-error #1 (pwdd)

Plain English: **the computer searched all its standard places and found
no program called `pwdd`.** The two likely causes:

1. **A typo** — you *meant* `pwd` (the classic: muscle memory adds a
   letter).
2. You meant a different tool that isn't installed yet.

Since `pwdd` isn't a thing, fix it by retyping correctly:

```
pwd
```

*The lesson:* "command not found" is nearly always the computer *spelling
your word back to you for a second look* — so give it the second look.
This error never damages anything; it's purely informational.

## Exercise 7 — Read-the-error #2 (terminal_practise)

The **two-part cause**:

1. **Wrong name**: the folder is `terminal-practice` (with a hyphen, from
   Chapter 9's lesson), and you typed `terminal_practise` — underscore,
   and the British-spelling
   "practise." Two honest slips, and the second one is the kind your brain
   makes when it's recalling a word instead of reading it.
2. Standing in **the right place** (home folder), so location isn't the
   problem here — *name* is.

The **two-part fix**:

```
ls
```

...to check the actual name of the folder on disk, then:

```
cd terminal-practice
```

...typing it exactly as `ls` shows it.

*The lesson:* "no such file or directory" invites **two questions**, not
one: *is the name right?* — *and am I in the right folder?* Here it's the
name; Exercise 3's `cd Documents` problem was the location. Both flavors
of the same error, both fixed by `ls` + `pwd` in ten seconds.

## Exercise 8 — Verify installs

```
ollama --version
```

```
python3 --version        # Mac/Linux
py --version             # Windows
```

*Why:* `--version` is the polite, universal "are you there?" flag for
almost every command-line tool ever made. It changes nothing, prints
nothing scary, and gives a clean yes/no with a nice bonus (the exact
number).

**Gotcha addressed:** if Python's version command fails on Mac/Linux,
try `python --version` (no 3) — some Macs are configured that way. On
Windows, `py` is the launcher that almost never fails when Python is
installed at all.

## Exercise 9 — Pip's quiet news

```
python3 -m pip list          # Mac/Linux
py -m pip list               # Windows
```

*Why:* `list` is pip's inventory command. The `-m pip` middle section is
the careful way to ask *Python* to run its own pip, which sidesteps
several confusing Mac/Windows path quirks mentioned in Chapter 6.

**Gotcha addressed:** the list is *long* — Python installs with dozens of
built-in packages before you ever installed anything. Seeing 60 lines is
normal, and **none of it is alarming.** Scan for `emoji` (from Chapter 6)
with your eyes, or filter with your tool of choice later. ("Requirement
already satisfied" from Chapter 6 is the same calmness: lots of news,
little of it urgent.)

## Exercise 10 — One-line Python

```
python3 -c "import datetime; print('Python +', datetime.datetime.now())"
```

(Windows: `py -c "..."` — same quotes.)

Expected, roughly: `Python + 2026-10-25 09:41:02.114233`

*Why this is a milestone:* `python3 -c` runs **one line of Python
without a file** — the fastest possible "can Python hear me?" test. This
one pattern is the beginner's universal trick for checking that a
package installed in Chapter 6 actually *works* (`python3 -c "import
emoji; print(emoji.emojize(':sparkles:'))"` was the same pattern at
work).

**Gotcha addressed:** the quotes matter — Python wants the string after
`-c` wrapped in quotes, and your terminal wants to hand Python the whole
thing as one piece. Inside that quoted string, semicolons let you put
two Python statements on one line. `import` then `print` — the same two
moves from your first script, compressed.

## Bonus — The fear extinguisher (Mac/Linux)

```
sudo -v
```

asks for your password and simply *verifies* your admin status — no
side effects, no changes, no log entries beyond your own history.

```
sudo -k
```

clears that verified state immediately — like stepping back out of the
admin zone you were only peeking into.

*The lesson:* `sudo` is a **doorway you choose to use**, not a status
que you're granted. This pair of commands lets you *practice* that
doorway with absolutely zero consequences — the exposure therapy in the
[FAQ](faq.html) in action. On Windows, the analogue is deliberately
*not* opening PowerShell as Administrator, and knowing that Chapter 4's
commands don't need it.

---

Done! If any answer surprised you, that exercise was the one worth
re-practicing. Then [glossary →](glossary.html) for all the words, or the
[FAQ](faq.html) for the fears.
