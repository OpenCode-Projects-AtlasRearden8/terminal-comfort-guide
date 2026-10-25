# Chapter 2 — Moving Around: Folders, Paths, and Not Getting Lost

Now that you can open a terminal, let's make you a navigator. This chapter is
the one that pays for itself first, so go slow and type everything.

## The big idea: the terminal lives *inside* a folder

Here's the thing nobody tells beginners: your terminal is always sitting
inside one specific folder, the same way you're always in one room of your
house. When you run a command, it happens *in that folder* — like calling out
into the hallway from wherever you're standing.

You can always ask **w**h**e**re a**m** **I**... actually, you have a shortcut
fingers:

```
pwd
```

`pwd` stands for **p**rint **w**orking **d**irectory ("directory" is
computery for "folder"). Try it. You'll see something like:

- Windows: `C:\Users\YourName`
- Mac: `/Users/yourname`
- Linux: `/home/yourname`

That's your **home folder** — the main room where your personal stuff lives.
The terminal starts you off there every time on purpose.

(On macOS and Linux the command is the same name for the same directory, but
on Mac it sometimes prints `/Users/yourname` instead of `/home/yourname` —
same idea, different house layout. Windows writes its directories starting
with a drive letter like `C:` and uses `\` between folders; Mac and Linux use
`/`. Those slashes are called **separators**, and knowing which one your
machine uses is half of not getting lost.)

## Looking around: `ls` and `dir`

To see what's in the folder you're standing in:

- Mac / Linux (and Windows Terminal too, these days):

```
ls
```

- Windows (older Command Prompt dialect):

```
dir
```

`ls` is short for **l**i**s**t. You'll see your actual folders and files —
Documents, Downloads, maybe some things you forgot existed. The computer is
just reading the room to you.

> **Friend note:** if `ls` feels like a misspelling, you're right, sort of —
> it's Unix tradition, from programmers who hated typing. Windows eventually
> added `ls` to PowerShell because everyone else liked it. Either way: it
> lists things, it changes nothing. Safe to run ten times a day.

## Walking: `cd`, and the two magical names

To **c**hange **d**irectory (move to another folder):

```
cd Documents
```

That means: "move into the folder called Documents, starting from where I'm
standing." Run `pwd` again and you'll see you *moved*:

- Mac/Linux: `/Users/yourname/Documents`
- Windows: `C:\Users\YourName\Documents`

Some things to know as you walk:

1. The terminal remembers. You don't "open" a folder like with a window; you
   *walk* into it, and you stay there until you walk elsewhere.
2. Folder names with spaces need quotes: `cd "My Documents"` (though plain
   `cd Documents` works if it's the real Documents folder on Mac, or if yours
   has no space).
3. Names have to match exactly, capital letters and all. `cd documents`
   fails if the folder is named `Documents`. The computer isn't mad at you;
   it just takes you literally.

Now, two magical folder names that work everywhere:

- `.` (one dot) means **this folder, the one I'm in**.
- `..` (two dots) means **the folder one level up** (the hallway outside this
  room).

So:

```
cd ..
```

takes you back up one level. And this one is the "I want to go home" button:

```
cd
```

Yes — bare `cd` with no destination. On Windows *and* Mac *and* Linux, typing
`cd` and pressing Enter returns you to your home folder. When you get lost —
and you will, today probably — `cd` is your reset button. Memorize it.
Serious memorize it. It is the single most fear-reducing command in this
manual.

## A path is just an address

When you see text like `/Users/you/Documents/journal.txt`, that's a **path**:
an address, from the outside door to a specific file. Two flavors exist:

- **Absolute path**: starts from the very top (`/Users/...` or
  `C:\Users\...`). Works from anywhere, like a full postal address.
- **Relative path**: starts from where you're standing (`cd Documents` means
  "from here, go into Documents"). Works only from where you are, like
  "turn at the second hallway."

Both are normal. Mix them freely. If a command in a tutorial says
`cd ~/Documents`, the `~` is anickname for your home folder: "my home,
then Documents." (Remember that `~`? It was in your prompt. Now you know it
by name.)

## `clear` and the tidy-up

When your screen gets crowded with old output:

```
clear
```

...clears the visible screen (on Windows, `cls` does the same). This deletes
*nothing*. It's like wiping a whiteboard — the room is still the same room;
you just can't see the old chalk dust anymore. Totally safe, infinitely
reversible.

## Your homework: a five-minute walk

Do this walk in your terminal, in order. It's completely safe — you're only
moving, never changing anything:

```
pwd
cd ..
pwd
cd ..
pwd
cd
pwd
ls
cd Documents
pwd
cd
```

What happened, chapter by chapter of your walk:

1. You saw where you started.
2. You walked up into the hallway (one `..`).
3. And into the next hallway up (another `..`).
4. You gave up on the stairs and teleported home with bare `cd`.
5. You confirmed you're home.
6. You listed what's in your house.
7. You stepped into Documents.
8. You went home again, because muscle memory is the real lesson.

If any step surprised you, run it again. That's it. That's the whole skill:
**pwd to know where you are, cd to walk, cd alone to go home, ls to see
what's around.** Four commands and you cannot get permanently lost. In
[Chapter 3](ch-03-safe-copy-paste.html) we'll cover the one genuinely
sneaky thing in terminal life: pasting text from the internet.
