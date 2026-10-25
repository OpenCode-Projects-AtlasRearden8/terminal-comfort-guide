# Glossary — Every Word, Plainly

Every term used anywhere in this manual, one definition each, no
dictionary smugness. Live link-backs from the chapters land here, so
bookmark it if that's your style.

| Term | Plainly |
| --- | --- |
| **absolute path** | A file/folder address that starts at the very top of your disk (`/Users/...` or `C:\...`). Works from anywhere, like a full postal address. (Chapter 2) |
| **admin / administrator** | The mode (or user) allowed to change things that belong to the *whole* computer, not just to you. Used deliberately, usually with a password. (Chapter 8) |
| **argument** | The word(s) after a command that say what to act on. In `cd Documents`, `Documents` is the argument. (Chapter 4) |
| **command** | The name of a program, plus optional arguments and flags. One sentence to the computer. (Chapter 4) |
| **command prompt** | (1) The prompt in any terminal. (2) A specific, older Windows terminal program called "Command Prompt" (`cmd`). Distinguish by context. (Chapter 1) |
| **directory** | Official word for a folder. Same thing. (Chapter 2) |
| **error message** | The computer telling you exactly where what it saw didn't match what you asked. Information, not punishment. (Chapter 7) |
| **flag / option** | A little switch for a command, almost always starting with `-` or `--`, like `ls -a` or `--help`. (Chapter 4) |
| **local / local-first** | Running on *your computer*, with no internet required and nothing sent anywhere. Ollama models are local. (Welcome) |
| **`ls`** | "List" — show what's in the current folder. Safe to run as often as you like. (Chapter 2) |
| **`cd`** | "Change directory" — walk into a folder. Bare `cd` = go home. `cd ..` = one level up. (Chapter 2) |
| **`mkdir`** | "Make directory" — create a new, empty folder. (Chapter 9) |
| **model (AI)** | A file containing a neural network's learned settings ("brain file"), plus the code to run it. Small ones: a few GB. (Chapter 5) |
| **Ollama** | A friendly program that downloads and runs local AI models on your own machine, offline. (Chapter 5) |
| **package** | A bundle of ready-made code that pip can install for Python to use. (Chapter 6) |
| **PATH** | The list of standard folders where your terminal looks for programs by name. Miscount on PATH = "command not found." (Chapters 4 & 7) |
| **pip** | Python's built-in installer for packages ("pip installs packages"). (Chapter 6) |
| **PowerShell** | Windows' modern terminal-shell program — the one this manual assumes you're using on Windows. (Chapter 1) |
| **prompt** | The short text before the cursor in a terminal, meaning "the computer is listening," like `PS C:\Users\You>` or `you@mac:~$`. (Chapter 1) |
| **pwd** | "Print working directory" — show the full path of the folder you're currently standing in. (Chapter 2) |
| **`pip install NAME`** | Download and install a Python package by name. (Chapter 6) |
| **Python** | The programming language all the scripts in this manual use. Installed via python.org if not already on your machine. (Chapters 6 & 9) |
| **relative path** | An address that starts from where you're currently standing (`cd Documents`). (Chapter 2) |
| **`rm`** | "Remove" — delete a file or folder *permanently* (no trash bin). Respect it, always; read the whole line before Enter. (Chapter 4) |
| **root** | Unix's name for the all-powerful admin user; also the very top of the file system (which is why `/` is called "root"). (Chapter 8) |
| **script** | A file of instructions, saved with a name, that the terminal can run on request. A command is one sentence; a script is a paragraph. (Chapter 9) |
| **shell** | The program inside your terminal that actually listens, finds, and runs commands. Bash/zsh on Mac/Linux, PowerShell on Windows. (Chapter 4) |
| **`sudo`** | "Superuser do" — run the *next one* command as the administrator. Asks for your password. Mac/Linux. (Chapter 8) |
| **su** (mentioned only) | "Switch user" — older, scarier cousin of `sudo`. You won't need it in this manual. (Chapter 8) |
| **`tab completion`** | Press Tab to auto-finish a file/folder/command name you've half-typed. Massive safety and speed win. (Chapter 4) |
| **terminal** | The window/app where you type commands and see output. (Chapter 1) |
| **Terminal (Mac app)** | The specific Mac application you open with ⌘Space → `terminal`. (Chapter 1) |
| **`--version`** | The near-universal flag that asks a tool "are you installed, and which version?" Changes nothing. (Chapters 5, 6, exercise 8) |
| **`--help`** | The near-universal flag asking a command to explain itself. Always local, always free, always on your disk. (Chapter 4) |
| **`ollama run MODEL`** | Download (first time only) then start chatting with a named local model. (Chapter 5) |
| **`ollama list` / `ollama ps`** | "What brain-files do I own on disk?" / "what's running now?" (Chapter 5) |
| **`.py` extension** | The end of a script filename that tells Python (and you) "I contain Python code." (Chapter 9) |
| **`python3 -c "..."`** | Run one line of Python without making a file — the beginner's universal "is it working?" test. (Chapters 6 and exercise 10) |
| **`cd Documents`-style errors** | When a `cd` fails, check *name* (`ls` to see the real spelling) and *location* (`pwd` to confirm where you are). Two questions, ten seconds. (Chapter 7, exercise 7) |

Missed a word? That's a bug in the manual — the FAQ is the place to bring
it.
