# Chapter 11 — Practice Exercises (Do Them In Order)

Ten exercises. Every one can be done with what you learned in Chapters
1–9. Answers with full reasoning live in the
[answer key](ch-12-answer-key.html) — no peeking until you've tried. (You
can peek, of course. But you'll learn twice as much if your fingers try
first.)

**Setup reminder:** if you did Chapter 9, you have a `terminal-practice`
folder with `hello.py` in it. If not, make the folder now:
`cd`, then `mkdir terminal-practice`, then `cd terminal-practice`.

**Safety note:** none of these exercises delete anything, install
anything, or use `sudo`. Nothing here needs the internet after you're set
up.

---

### Exercise 1 — Orientation (from Chapter 2)

Open a terminal. Without looking back at Chapter 2, run **one command**
that answers "where am I right now?" Then run **one command** that
answers "what's in here?"

### Exercise 2 — The teleporter (from Chapter 2)

Starting from wherever you are, get to your home folder with **one
command**. Then verify you're home.

### Exercise 3 — A round trip (from Chapter 2)

Walk *into* a folder (any one you can see), confirm where you are, and
walk back out — one level up, not teleporting. Three commands total.

### Exercise 4 — Make and inspect (from Chapters 2 & 9)

In your home area, make a new folder called `my-notes`. Inside it, make a
second folder called `drafts`. Then list what's inside `my-notes` and
confirm both exist. (Hint: you can make two with two `mkdir` commands,
or trust `mkdir my-notes/drafts` — where have you seen slashes-as-inside
before?)

### Exercise 5 — First wave + a variable (from Chapters 1 & 3)

Run a command that makes the terminal say exactly:

```
I am learning, calmly
```

without typing an `echo` for each word. (One `echo` line total.)

### Exercise 6 — Read-the-error #1 (from Chapter 7)

You type:

```
pwdd
```

and get back an error on Mac/Linux:

```
zsh: command not found: pwdd
```

In plain English, what happened, and what are the two most likely causes?
(Not installation. Something simpler.)

### Exercise 7 — Read-the-error #2 (from Chapters 2 & 7)

You're standing in your **home folder**. You type:

```
cd terminal_practise
```

and get:

```
cd: no such file or directory: terminal_practise
```

Name the two-part cause and the two-part fix.

### Exercise 8 — Verify an install *before* installing more (from Chapter 5 or 6)

One command to check whether (a) Ollama is installed, and (b) Python
is installed. Two commands total — one for each.

### Exercise 9 — Pip's quiet news (from Chapter 6)

Run the command that lists the packages Python has installed **on this
machine right now**. Then name the package you installed in Chapter 6
(if you did that chapter's exercise).

### Exercise 10 — One-line Python (from Chapter 9)

Without creating a file, use the terminal to run a one-line Python
command that prints the current Python version *and* today's date.
(Hint: `python3 -c` runs one line of Python; Chapter 6 showed the
pattern. For the date part, Chapter 9 gave you the toolbox: `import
datetime` then `print(datetime.datetime.now())`.)

### Bonus — The fear extinguisher (from Chapter 8)

On Mac/Linux: run a command that *verifies* your admin status without
changing anything, then a command that *clears* that verified state.
Two commands, no changes, full explanation in the answer key.

---

When you've tried them (even unsuccessfully — that's how learning
works), check [Chapter 12 → the answer key](ch-12-answer-key.html).
