# Chapter 3 — Safe Copy-Paste (the One Genuinely Sneaky Thing)

So far, everything we've typed has been harmless. Now that you'll start
grabbing commands from websites (yay!) and downloading tools (Chapter 6), we
need to talk about paste. Copy-paste is the funnest AND the sneakest thing in
terminal life. This chapter is about the sneaky part — and the simple habit
that neutralizes it.

## Why paste is different from typing

When you *type* a command, your brain reads every character. When you
*paste*, 400 characters enter your terminal in zero seconds. Your eyes cannot
follow. The command starts running the moment you press Enter — and a
determined web page can make Enter press *itself*.

Here is the trick that a few bad-faith websites have played on people: some
pages can hijack your clipboard, so that what you *see* (`echo hi`) is not
what you *paste* (`rm something important`). This is rare and you'll almost
certainly never meet it — but one habit makes it irrelevant, so let's build
the habit.

## The gray-box rule

From now on, forever, follow one rule:

> **Only paste text into the terminal if it comes from a grey box you can
> read and understand the START and the END of.**

That means:

1. Read the *whole* command, not just the first word.
2. Notice where it begins and where it ends. No stray characters.
3. If you can't understand *all* of it, understand at least: is this doing
   something (a) safe, (b) reversible, or (c) to a real folder/file I own?

If a pasted command makes you go "wait, what does THIS word do?" — that's not
a failure, that's your brain working. Ask the glossary, ask a search engine
("what does curl -O do"), ask me in the FAQ. **Never feel bad about pasting
into a search engine before pasting into a terminal.** That's what
professionals do.

## Windows: pasting, the careful way

There's a lovely thing in Windows Terminal and PowerShell: **right-click**
pastes whatever's on your clipboard (Ctrl+V works too, in most cases). But
here's the kind setup for you: if you're using PowerShell, **the first
right-click paste of a multi-line paste just shows it and asks if you're
sure**. That prompt is your friend. Reading a command *before* Enter is the
whole game.

One more Windows subtlety: in some terminals, **Ctrl+V is NOT paste** — it
means something else (the literal letters Ctrl+V are verbatim-mode in some
shells!). If you paste and see weird letters appear instead of your text,
right-click instead. It's a quirk, not a mistake you made.

## Mac and Linux: the same, but friendlier

Ctrl+V on Mac/Linux is also usually not paste! Terminal paste is:

- **Mac: Cmd + V**
- **Linux: Ctrl + Shift + V**

(The extra Shift is the Unix folks' old way of saying "this is a paste, not a
control code.") If you paste and see nothing, try the other one. No harm
done.

## The brace-and-enter habit

When I was a beginner, every pasted command made me nervous. The fix was a
little ritual, and it takes four seconds:

1. **Paste.** (Don't press Enter!)
2. **Look** at the line. Does it match the grey box you meant to past? spaces,
   slashes, quotes — all there? No extra lines?
3. **Enter.**

That's it. Paste, pause, enter. Do it a hundred times and it becomes
automatic — and after a while you'll catch yourself pasting, reading a
command carefully, deciding *no*, deleting it, and finding a safer tutorial.
That's exactly the outcome we want. That's a person who isn't afraid of the
terminal anymore, just appropriately careful.

## One specific warning worth memorizing, and one reassurance

**The warning.** You will encounter, mostly in old forum posts, commands that
start with:

```
sudo ...
```

or, on Windows, "Run as administrator" buttons. Those commands are asking for
**special powers** (Chapter 8 covers this fully). They are **normal and
often fine** — but they deserve the brace-and-enter ritual *twice* as long.
Read them slowly. They can change system files, and "reversible" isn't
guaranteed there. If you don't understand it, don't be embarrassed — nobody
understands everything. Google it first or skip it.

**The reassurance.** Almost every command in this manual is the *opposite*
kind: `pwd, ls, cd, echo, clear` — none of those can change or delete
anything. Forgetting which is which is impossible if you just remember:
**walking and looking commands are always safe; installing and sudo commands
deserve a second read.** That single sentence is 90% of terminal safety.

## Your homework

1. Copy this line from this manual (select it, Ctrl+C / Cmd+C):

```
echo pasting on purpose, with awareness
```

2. Paste it into your terminal.
3. Do NOT press Enter yet. Read it. Confirm it's exactly what the grey box
   shows.
4. Now press Enter.

You just did the professional-grade thing. Most tutorials never even mention
this. In [Chapter 4](ch-04-running-things.html) we'll peek behind the curtain
at what a command even *is* — and why some words do more than others.
