# Welcome — Read Me First, Friend

## Hi. I'm glad you're here.

This little manual is for one kind of person above all: the person who has
heard the words "open a terminal" and felt their stomach drop a little.

Maybe you've watched a tutorial where someone types mysterious commands at a
black window and gets an AI running on their own computer in ninety seconds,
and you thought: *I could never.* Maybe you're a nurse, a teacher, a small
business owner, a writer — someone VERY good at complicated real-world things —
who just hasn't had a reason to learn this weird 1980s habit that suddenly
everyone in AI does.

**You can.** The terminal is not scary. It is a text box where a computer
listens. Everything here can be undone, backed out of, or simply closed. There
is no way you can break your computer by *reading* this manual, and almost
nothing you can break by following it either.

## What this manual will and won't do

**Will:**

- Show you, step by step, how to open a terminal on Windows, macOS, and Linux.
- Teach you to walk around your own folders without getting lost.
- Walk you through `ollama` (running small AI models on your own machine) and
  `pip` (downloading Python tools) **calmly**, at your own pace.
- Make error messages feel like helpful notes instead of sirens.
- Give you your first tiny script — one you'll fully understand — and practice
  exercises with a complete answer key.
- Explain `sudo` and "Run as Administrator" so you know when they're safe.
- Never require you to install anything before you understand what it is.

**Won't:**

- Give you 40 commands at once.
- Use jargon without defining it (every defined word lands in the
  [glossary](glossary.html)).
- Make you feel dumb. Ever.

## What "local-first" means here

This project is built to run **on your machine, with no internet connection
and no accounts**. The manual itself, the example script, and the tool that
turns this manual into a little website all live in this folder. When we get
to Ollama in [Chapter 5](ch-05-ollama.html), the whole point is that the AI
model runs on *your* computer — no data uploaded, no subscription, no magic.
If your internet dies halfway through this manual, the only casualty is the
download speed, not the lesson.

## The one promise before we start

I promise the following three things are true, and they change everything:

1. **The terminal is a conversation, not a test.** If you make a mistake, the
   computer tells you, and you try again. There is no permanent damage button
   in any command we use here.
2. **Every error message is information**, not punishment. By Chapter 7 you'll
   be able to read most beginner errors in about ten seconds.
3. **Nobody was born knowing this.** Every expert you've ever watched type
   confidently once googled "how to open terminal" with the same nerves you
   have.

## How to use this manual

Read chapters in order the first time. Each chapter takes 5–15 minutes. Every
command you see in a grey box like this:

```
pwd
```

is something you can **type yourself** (please type it, don't copy-paste —
typing is how your fingers learn, and Chapter 4 explains why copy-paste needs
care anyway). The chapters build on each other gently:

| Chapter | What you'll be able to do |
| --- | --- |
| [1](ch-01-open-a-terminal.html) | Open a terminal on your computer |
| [2](ch-02-moving-around.html) | Walk between folders and understand paths |
| [3](ch-03-safe-copy-paste.html) | Copy-paste without surprises |
| [4](ch-04-running-things.html) | Understand what "running a command" really is |
| [5](ch-05-ollama.html) | Run a tiny AI model on your own machine |
| [6](ch-06-pip.html) | Install Python tools calmly |
| [7](ch-07-reading-errors.html) | Read error messages like a friend |
| [8](ch-08-admin-and-sudo.html) | Know when admin rights are OK |
| [9](ch-09-first-script.html) | Write and run your first script |
| [10](ch-10-where-next.html) | Know where to go next |

Then there are [10 practice exercises](ch-11-exercises.html) with a complete
[answer key](ch-12-answer-key.html), a [glossary](glossary.html) of every term
used here, and a [fear-reducing FAQ](faq.html) that answers the questions
you're too nervous to ask.

Take a breath. Type your first command soon. Let's go.

*— written in the plain-English spirit of*
[*Dylan Asdale / ASDALE DYNAMICS, LLC*](https://dylanasdale.github.io)
