# Chapter 6 — pip: Installing Python Tools Calmly

If Ollama was the big thrill, `pip` is the quiet workhorse. Nearly every
beginner AI tool, script, and utility lives in the Python world, and `pip`
is how Python installs them. Same three moves as Chapter 5: **install it
once, ask what you have, install named things.**

## What pip is, in one paragraph

Python (the programming language all your future scripts will use) comes
with a built-in helper called **pip** — short for "pip installs packages" —
which downloads ready-made code bundles ("packages") from a giant public
library site called PyPI. Think of it as an app store, except free, without
accounts, and slightly more old-fashioned. When you `pip install` something,
you get the code folder placed somewhere Python can find it. That's the
whole event.

## Step 1 — Check you have Python (which means you have pip)

Type this (Mac/Linux):

```
python3 --version
```

or on Windows:

```
py --version
```

Expected: something like `Python 3.13.5`. Great, you have Python, and Python
mathematically guarantees pip comes along (they're shipped as a pair these
days).

If that command failed: no shame — Windows doesn't always ship Python. Go to
[python.org/downloads](https://www.python.org/downloads/), download the
latest Python 3 installer, run it like Ollama in Chapter 5, and **make sure
you check the little checkbox that says "Add Python to PATH"** during
install — that checkbox is the difference between "works" and Chapter 7's
most common beginner error. (If you forgot the checkbox, simply run the
installer again and check it.)

Then type:

```
python3 -m pip --version
```

(or `py -m pip --version` on Windows). If you see a version number, pip is
real and present. That `-m pip` middle part is just the careful way to
call pip "through" Python itself, and it's what the rest of this chapter
uses, because it avoids a whole category of confusing Mac/Linux mix-ups.

## Step 2 — Your first calm install

Here's a tiny, useful, totally-real package to break the seal on:
`emoji` — yes, the emoji library, because learning should be a little
delightful. Actually, let's pick something you'll actually care about in a
minute: we'll use plain stdlib Python in our Chapter 9 script and install
**nothing** — but for the *muscle memory*, do install this one:

```
python3 -m pip install emoji
```

(Windows: `py -m pip install emoji`.) You'll see text roll by that looks
like this, roughly:

```
Collecting emoji
  Downloading emoji-2.x.x-py2.py3-none-any.whl (xxx kB)
Installing collected packages: emoji
Successfully installed emoji-2.x.x
```

Read that like a friend: it *collected* the package, *downloaded* it, and
*successfully installed* it. No prompts, no fees, no pop-ups, no cloud
account. It's in a folder somewhere; Python can now find it.

## Step 3 — The pip survival kit

Five commands cover 95% of beginner life:

```
python3 -m pip install NAME   # install a package by name
python3 -m pip list           # what do I have installed?
python3 -m pip show NAME      # details about one package
python3 -m pip uninstall NAME # remove one package
python3 -m pip help           # the official manual, on your disk
```

Same shape as Ollama's kit, notice: **list / run / remove.** Once you've
seen this pattern twice, every future tool on Earth feels familiar.

## Step 4 — Verify it worked (the satisfying part)

```
python3 -c "import emoji; print(emoji.emojize('it worked! :sparkles:'))"
```

Should print: `it worked! ✨`

What that line means, slowly: `python3 -c` means "run this one little piece
of Python and stop." `import emoji` means "find my installed emoji package
and load it." `print(...)` shows you proof on screen. If that little sparkle
showed up, you have just completed a full software-development loop —
install, import, run — that professional programmers repeat ten thousand
times in their lives.

## Two beginners' rules that will save you later (gently noted, not feared)

1. **Install commands deserve the Chapter 3 pause.** `pip install` and its
   cousins are *change* commands. Read what name you're actually typing
   (not `emogi`, not `emjoji`). Wrong names either error out harmlessly or,
   worst case, install a package you don't want — which `pip uninstall`
   fixes. Rule of thumb: only install packages whose names you can see
   spelled correctly in a trustworthy place.
2. **"Requirement already satisfied" is not an error.** If pip replies that
   way, it means the package was already on your disk. Success, announced
   boringly. Most of what looks like a problem in terminal output is just
   the terminal being extremely literal.

That last sentence is the thesis of [Chapter 7,
friends](ch-07-reading-errors.html): error messages are almost never
punishment — they're **extremely literal descriptions of what didn't match**.
We'll make you able to read them in one short sitting.
