# FAQ — Fear-Reduced

The questions people are actually carrying. Warm answers, no
condescension, no fake promises. Written mostly for the person who has
been putting off opening a terminal for *months* — yet read this far
anyway. Hi, you made it.

## Am I going to break something?

Let's take this seriously, because it deserves more than "no."

- **Reading** (`pwd`, `ls`, `cat`-style looking, this manual) can't break
  anything, ever.
- **Walking** (`cd`, `mkdir`) can't break anything — mkdir makes empty
  rooms; cd just moves you.
- **Installing** (Ollama, pip) can't break your computer. Worst
  realistic case: you don't like it, you delete it, disk space is back.
- **Changing/deleting** (`rm`, deep system edits) *can* break things —
  and this manual never asks you to do either of those without walking
  you through it to your own created files. The fear-reducing fact is
  that these two categories are *visibly different* in every command
  you'll ever see: `rm`, `del`, `format`, "Run as Administrator" always
  announce themselves.

So the honest full answer is: **you cannot break something by following
this manual, and you cannot break your computer with a look-and-walk
command set.** The categories are learnable in one afternoon, and you've
already learned them.

## I opened a terminal and had no idea what to type. Is that normal?

Yes, universally. Everyone who has ever learned this stared at the
prompt feeling exactly like that. The fix isn't inspiration; it's what
you did in Chapter 1 — one `echo` command, felt the conversation, noticed
nothing electrocuted you. That's the whole trick of this manual, and it
works within ten minutes more reliably than people expect.

## Do I have to memorize commands?

No. Real professionals google syntax constantly. What you DO memorize —
slowly, by doing — is a *rhythm*: pwd/ls/cd, echo, the paste-look-enter
habit, reading the LAST line of errors. That rhythm fits in your hand,
not just your head, and it's what Chapter 2's homework was actually
installing in you.

## The blinking cursor scares me. It's like it's judging me.

It isn't. It's less like a judge and more like a cat sitting beside you,
waiting. The computer is *patient*, not judging. It has no opinion, no
memory of your mistakes across closures, and infinite patience. It was
literally designed to wait all day for a slow typist and never sigh.

## Is local AI actually safe? What could go wrong?

Model files are just files. They can't listen to your microphone, watch
your screen, or phone anywhere — the model has no network code; Ollama
serves chat to *your machine* only. The realistic risks are mundane:
disk space (model files are GBs) and RAM. Both are visible (`ollama
list`, `ollama ps`) and reversible (`ollama rm`, close the chat). Versus
cloud AI, the *privacy* direction runs the other way entirely: local
means nothing leaves.

## Why is nothing appearing when I type my sudo password?!

Because Unix deliberately hides it: no dots, no stars, nothing. It is
receiving your keystrokes. Type it and press Enter. (This is Chapter 8's
most-read sentence. It's fine.)

## My output looks different from the answers here. Am I in trouble?

Probably not. Output varies by system name, folder contents, terminal
theme, OS version, phase of the moon. What matters is *shape*: a path
with slashes, a list of names, an English-language error. If the *shape*
matches but the text is different, you're fine. If the shape is entirely
absent, that's a real Chapter 7 lookup ("paste exact phrase into a
search engine").

## Can I notice my typing is wrong and edit it before pressing Enter?

Yes! Left/right arrows move the cursor within the line. Backspace works.
So does Home/End. The terminal is a *document you're drafting*, and
Enter is "I said what I said" — perfectly fine to draft for ten seconds
first. The one surprising thing: some shells offer up-arrow to recall
your previous command. Try ↑. It's lovely, and it's how professionals
re-run and tweak instead of retyping.

## What if I press Ctrl+C by accident and everything stops?

Ctrl+C means "stop the current command." That's its job. If you pressed
it during `ollama run` or a long download, you *interrupted* — Ollama
will resume/fine afterward; downloads are partially cached; nothing is
broken. If it happens when nothing was running, your shell just hummed
and gave you a fresh prompt. Ctrl+C is not a panic button; it's a
polite "hold on."

## I feel slower than everyone else I watch on tutorials.

You're a nurse, or a parent, or someone excellent at other hard things.
The terminal is *a third language* you're picking up in the margins of
your real life. Slow and regular, like the exercises and Chapter 10's
advice, is not a compromise — it's *the* way this actually sticks for
adults with full lives. Speed-chasing is how you end up back at fear.

## What's the difference between "admin", "sudo", and "Run as Administrator"?

The same idea in three dialects: permission to change computer-wide
things, granted through a password (sudo on Mac/Linux) or an
elevated-confirmation window (Windows). Chapter 8 is the full tour.

## Can I do all of this offline?

Everything in this manual except the *initial downloads* (Ollama
installer, model file, pip packages required by Python itself). After
those land on disk, the terminal, the manual's website, your script, and
your local AI all work with the actual internet cable removed. That's
the "local-first" promise, kept.

## Is this manual really free? Is anything being collected?

Free, MIT-licensed (see the `LICENSE` file in this project), and the build
system that
turns these chapters into a website runs *on your machine in seconds
with no dependencies* — the `scripts/` folder is done in plain
Python, no cloud involved, no telemetry, nothing to install. You can
read every line of this whole project in an hour and it will never send
or store a byte.

## I did everything up to here. Do I get a sticker?

You get better: you're someone with a practice folder and a working
local AI on your own machine, while other people are still afraid of a
blinking cursor. Print out that and stick it anywhere. Well done,
friend.
