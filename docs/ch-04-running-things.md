# Chapter 4 — What "Running a Command" Really Is

You've run `pwd`, `ls`, `cd`, `echo`. Time to pull back the curtain. Not to
overwhelm you — to *demystify*. Once you see what a command actually is, the
terminal loses its last bit of magic (in a good way).

## A command is just a program's name

Every single command you type is a **name of a program**, followed by
optional **words** for it to pay attention to:

```
command-name  word1  word2
```

That's it. That's the whole grammar. `echo hello`: the program `echo`, given
the word `hello`. `cd Documents`: the `cd` behavior, aimed at the word
`Documents`.

Words after the command have two flavors:

- **Arguments**: the main "what to do it to."
- **Flags/options**: little switches, almost always starting with `-`
  (one dash) or `--` (two dashes). Like `ls -a` (also show hidden files) or
  `ls --help` (show this command's own instructions).

You've already used an argument without noticing: in `cd Documents`, the word
`Documents` was the argument.

## Where do these programs even live?

Fair question. When you type `ls`, the terminal doesn't have code for it
inside itself. It **looks for a program with that name** in a list of
standard places on your computer, and runs it. That list of places is called
the **PATH** (you'll meet it again when something goes wrong in Chapter 7).

The practical upshot, and it's a good one for beginners:

- Commands like `ls`, `pwd`, `echo` were shipped with your operating system.
  They live where your OS expects them, and the terminal always finds them.
- New commands (Ollama, pip, Python) have to be *installed* — which literally
  means "put an extra folder of programs somewhere on your disk and tell the
  terminal about it." We do that carefully in the next two chapters.

## Reading command help is a superpower

Every command in the universe — every single one — is willing to explain
itself. Two ways to ask it for help:

```
ls --help
```

(Mac/Linux; shows a dump of what `ls` can do.) On Windows:

```
Get-Help Get-ChildItem
```

(That's PowerShell's fancier name for the `ls` command; and yes, one of the
real names of Terminal on Windows is "the PowerShell shell doing ls under a
stage name." It'll make sense later.)

Don't even try to *read* all of that help text yet. Right now the win is
just: **the manual is on your machine, not mine.** When you wonder "can `ls`
show file sizes?" you can find out locally, instantly, offline. That's what
local-first really means.

## The "am I allowed to?" rule — read-only vs. changes

By now you know some commands that look around (`pwd`, `ls`) and some that
move *you* (`cd`). Both are safe in one important sense: they don't change
your files. The commands that actually **change** things — installing,
deleting, writing files — look different, and there's a small set of patterns
to recognize:

- Installing something: usually the word `install` appears.
- Deleting something: on Mac/Linux, `rm` (short for *remove*) —
  **treat `rm` with respect always, even as a beginner**, because it
  deletes straight to nowhere (no trash bin). If you do the exercises in
  this manual, you'll practice with a make-believe folder first.
- Writing a file: usually you'll *see* the file being made discussed, not a
  surprise.

The only genuinely dangerous plain command you'll encounter as a beginner is
deleting files with `rm`. Here's your friend rule for it, and pasting too:

> **If a command contains `rm` (or `del` on Windows), and you didn't write it
> yourself just now, stop and read the whole line. Only proceed if you can
> name exactly which file(s) it points at.**

We will NOT need `rm` in this manual except to clean up after our own
practice, which we do in Chapter 9's setup, with a file *we* created on
*purpose*.

## What "the shell" means (one paragraph, then dessert)

The terminal program you've been typing into is technically called a **shell**
— the layer *around* your computer that takes your words and does the
looking-up and running. Mac and Linux give you a shell called `bash` or
`zsh`. Windows gives you `PowerShell`. Different accents, same personality.
Every chapter here works identically across all of them (I'll flag it when
one doesn't).

Dessert: **tab completion.** Type `cd Doc` and press the **Tab** key. The
shell finishes `Documents` for you. This works for folder names, file names,
command names — and it's not cheating; professional programmers use it
constantally. It's also the top safety tool: completing a real name means
you never mistype `rm Documents` into `rm Doccuments`.

That's the theory you needed. Next chapter: installing a real tool
(`Ollama`) and meeting your first AI that runs **on your own computer,
unplugged**.
