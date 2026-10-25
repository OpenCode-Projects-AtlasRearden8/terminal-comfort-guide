# Chapter 5 — Ollama: Running a Tiny AI on Your Own Computer, Calmly

This is the chapter the whole manual exists for. Take your time. Nothing
here breaks anything; several steps are just *waiting*.

## What Ollama is, in one paragraph

[Ollama](https://ollama.com) is a friendly program that lets your computer
run small AI language models **locally** — meaning: the model's "brain" is a
file on your disk, the chat happens inside your machine, and nothing you
type leaves your computer. No account, no API key, no subscription, no cloud.
When it's running, you could unplug your router and it would keep
working. That's what **local-first** AI feels like: it's *yours*.

Important expectation-setting: a small local model is more like a smart,
quick friend than a super-expert. Beginner-friendly local models won't write
your whole book. But they're perfect for first contact: you get to *talk to
an AI with no internet at all*, and that feeling changes how you think about
all of this.

## Step 1 — Install Ollama

Windows:

1. Go to [https://ollama.com/download](https://ollama.com/download).
2. Download the Windows installer (a normal `.exe` file).
3. Double-click it, click through like any ordinary app install.
4. When done, **open a fresh terminal** (Chapters 1 & 4 — restart so the
   terminal sees the new program).

Mac:

1. Same download page; get the Mac version (a `.dmg` or `.zip` depending on
   your chip).
2. Drag it into Applications like any Mac app.
3. **Open a fresh terminal.**

Linux (one honest mention of a command that looks scary and is fine):

```
curl -fsSL https://ollama.com/install.sh | sh
```

Deep breath. What does this do? `curl` = a program that downloads things.
`-fsSL` = flags meaning "quietly, but fail loudly if something's wrong."
`https://ollama.com/install.sh` = the official install script. `| sh` =
"and then run that script with the shell." This is a *very* common Linux
pattern. It's exactly the kind of command our Chapter 3 rule is for: you
know where it comes from (yes, the official site — check the address in your
browser before pasting), what it does (installs Ollama), and what happens if
it fails (it prints an error, changes nothing else). Failed installs leave
your system exactly as it was.

## Step 2 — Prove it's there

Open your (fresh) terminal and type:

```
ollama --version
```

If you see something like `ollama version is 0.x.y`, beautiful — it found
the program. You just installed a piece of real software, and the terminal
can see it. That's a real milestone. (If the terminal says `command not
found` — that's a solvable hiccup, and Chapter 7 covers exactly that, but
the short version is: close the terminal and open a new one, and if that
doesn't work, reinstall.)

## Step 3 — How big a model can you run?

Local models come in sizes, named like clothes: tiny models are a few
**gigabytes (GB)**, bigger ones get much larger. The size numbers you'll see
next to model names (like `1b`, `7b`, `8b`) roughly mean "billions of
little number-settings inside the model's brain" — more settings,
smarter-sounding, bigger download, slower replies.

Rule of thumb from a friend:

- **4 GB of free RAM** (most normal laptops from ~2018 on): you can run a
  small model. It'll be chatty but genuinely useful.
- **8 GB or more RAM**: you're comfortably in beginner territory.
- **16 GB+**: consider a "medium" model later. Not needed today.

How big is Ollama's smallest-class beginner model? Around **1–2 GB to
download.** Download once, keep forever, use offline.

## Step 4 — Download and run your first model, in one command

Type this:

```
ollama run llama3.2:1b
```

What happens next:

1. First time: a **download progress bar**. This is the "brain file"
   arriving. Depending on internet speed this is minutes of waiting, and
   that is *fine* — go get coffee. It's one file; when it's done you're done
   forever on this machine.
2. Then: a **chat prompt** appears, something like `>>>`. The computer is
   now asking YOU something for once.
3. Type anything conversational: `Hello! What are you?` and press Enter.
4. It answers. On your computer. Offline-capable. No account.

When you're done playing, end the chat with:

```
/bye
```

and press Enter. You're back at your normal terminal prompt. Nothing was
installed "deep" anywhere weird; you just downloaded one file and talked to
it.

## Step 5 — The calm Ollama survival kit

Six commands make you competent. That's all.

```
ollama --version        # is it installed?
ollama list             # what brain-files do I have on disk?
ollama run llama3.2:1b  # start a chat with a specific brain
ollama ps               # is a model running right now?
ollama stop llama3.2:1b # politely end a running chat session
ollama help             # the official list of all the above
```

See how only `run` downloads anything, and it only downloads the model you
name? Deleting a model later (caring about disk space) is
`ollama rm llama3.2:1b` — the same `rm` respect from Chapter 4 applies: it
removes only the model file, nothing else, and you can always re-download.

## Why this matters more than it seems

Everything in your future AI-learning life builds off the same three moves
you just did: **install once, list what you have, run a named thing.** Ollama
is the friendliest possible version, and it's the gateway to *local AI* as a
concept — the strongest privacy-respecting branch of AI right now, and the
one that's genuinely yours.

In [Chapter 6](ch-06-pip.html), we meet `pip`, the Python version of the
same friendliness. Then Chapter 7 teaches you to read error messages so that
`command not found` — that friendly hiccup you may already have met — never
scares you again.
