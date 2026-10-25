# Chapter 1 — Opening the Terminal (Windows, Mac, Linux)

The terminal is a program that lives on your computer right now. You don't
need to install it. You only need to find it. Below are three sets of
instructions; do the one(s) for your computer, and skip the others.

## Windows

Windows actually has *two* terminal programs. Either works for this manual,
but the newer one is nicer:

**Way 1 (newest and best): Terminal app**

1. Press the **Windows key** (bottom row of your keyboard, has the little
   window logo).
2. Type the word `terminal`.
3. Press **Enter**.

A window opens. It may show you tabs, or a single prompt that ends with `>`
and a blinking cursor. That cursor is the computer waiting politely for you.
That's it — you've opened a terminal.

**Way 2 (slightly older, totally fine): PowerShell**

1. Press **Windows key** again.
2. Type `powershell`.
3. Press **Enter**.

You'll see something like:

```
PS C:\Users\YourName>
```

Read that out loud: "Here I am, not PowerShell us, the computer, under the
folder C, backslash (Windows' way of writing a slash), Users, YourName, your
turn." You'll learn to read prompts without fear in Chapter 2.

> **Friend note:** if you install the *Windows Terminal* app later, great, or
> just wait and do it later. Windows 10 and 11 both have
> PowerShell already — that's all you need for everything here. One caution:
> avoid the very old program called "Command Prompt" (`cmd`) when it asks for
> PowerShell-style commands, because it speaks a slightly different dialect of
> the same language, and some commands from later chapters won't translate.

## macOS

The terminal program on Mac goes by its old Unix name: **Terminal**.

1. Press **Command + Space** (the two keys together). A search box called
   Spotlight appears in the middle of your screen.
2. Type `terminal`.
3. Press **Enter**.

A white (or translucent, if your Mac is feeling fancy) window opens with a
prompt that ends in `$` and a blinking cursor. Example:

```
yourname-macbook ~ %
```

or, on some setups:

```
Yournames-MacBook-Pro:~ yourname$
```

The `~` there means "your home folder." More on that in Chapter 2.

**Alternate route** (useful to know): open **Finder → Applications →
Utilities → Terminal**. Same program, same result.

## Linux

If you're on Linux, you're going to get the most warm congratulations — you
almost certainly already have a terminal, and your whole system was built
around it.

- **Ubuntu / GNOME**: press **Ctrl + Alt + T**, or press the Super key (it
  looks like the Windows key) and type `terminal`, then Enter.
- **KDE**: press Alt + Space and type `konsole`, Enter.
- **Any distro**: look for a program called *Terminal*, *Konsole*,
  *GNOME Terminal*, or *xterm* in your applications menu.

The prompt usually ends with `$`, like:

```
you@yourmachine:~$
```

Same as the Mac: `~` means your home folder. Different desktop versions make
tiny differences in how it looks; don't worry — the *commands* we learn are
the same everywhere.

## What you're actually looking at

Every terminal, on every system, has three parts:

1. **A prompt** — the short text before the cursor, which means "the computer
   is listening."
2. **A cursor** — the blinking line. Where your typing appears.
3. **Everything else** — output from commands you've run. This scrolls.

That's the whole interface. No menus, no tabs (okay, sometimes tabs), no pop
ups. Text in, text out.

## First command: just wave at it

Now type this and press **Enter**:

```
echo hello
```

You'll see:

```
hello
```

Congratulations, for real: you just told a computer to do something and it
did it. `echo` is the terminal's "repeat after me" command. Useless on its
own, and perfect for a first wave.

Then try:

```
echo the computer and I are getting along
```

It repeats everything after `echo` back. See? A conversation.

## Closing it, and the anxiety dissolve

To leave, you can:

- just click the X in the corner like any other window, or
- type `exit` and press Enter.

Nothing is "lost." Nothing "needs saving." The terminal is not a document;
it's a room you walk into and out of. Closing it with the X is exactly as
safe as closing a calculator app.

## Your tiny homework (2 minutes)

Open your terminal and run these two commands:

```
echo good morning terminal
echo good morning terminal
```

Twice on purpose. Once feels like luck; twice feels like knowledge. In
[Chapter 2](ch-02-moving-around.html) we'll walk around inside your own
computer — from the comfort of never leaving your chair.
