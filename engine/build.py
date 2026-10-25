#!/usr/bin/env python3
"""Build the Terminal Comfort Guide static HTML site from docs/.

Local-first and zero-dependency: plain Python 3 standard library only.

Usage:
    python3 engine/build.py            # build into ./site
    python3 engine/build.py --out DIR  # build into a different folder
    python3 engine/build.py --check    # build to a temp dir, verify links
"""

import argparse
import html
import re
import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
DEFAULT_OUT = ROOT / "site"

CHAPTERS = [
    ("index.html", "00-welcome.md"),
    ("ch-01-open-a-terminal.html", "ch-01-open-a-terminal.md"),
    ("ch-02-moving-around.html", "ch-02-moving-around.md"),
    ("ch-03-safe-copy-paste.html", "ch-03-safe-copy-paste.md"),
    ("ch-04-running-things.html", "ch-04-running-things.md"),
    ("ch-05-ollama.html", "ch-05-ollama.md"),
    ("ch-06-pip.html", "ch-06-pip.md"),
    ("ch-07-reading-errors.html", "ch-07-reading-errors.md"),
    ("ch-08-admin-and-sudo.html", "ch-08-admin-and-sudo.md"),
    ("ch-09-first-script.html", "ch-09-first-script.md"),
    ("ch-10-where-next.html", "ch-10-where-next.md"),
    ("ch-11-exercises.html", "ch-11-exercises.md"),
    ("ch-12-answer-key.html", "ch-12-answer-key.md"),
    ("glossary.html", "glossary.md"),
    ("faq.html", "faq.md"),
]

TOC_LABELS = [
    ("index.html", "Welcome"),
    ("ch-01-open-a-terminal.html", "1. Open a Terminal"),
    ("ch-02-moving-around.html", "2. Moving Around"),
    ("ch-03-safe-copy-paste.html", "3. Safe Copy-Paste"),
    ("ch-04-running-things.html", "4. What a Command Is"),
    ("ch-05-ollama.html", "5. Ollama (Local AI)"),
    ("ch-06-pip.html", "6. pip (Python Tools)"),
    ("ch-07-reading-errors.html", "7. Reading Errors"),
    ("ch-08-admin-and-sudo.html", "8. Admin &amp; sudo"),
    ("ch-09-first-script.html", "9. Your First Script"),
    ("ch-10-where-next.html", "10. Where Next"),
    ("ch-11-exercises.html", "11. Exercises"),
    ("ch-12-answer-key.html", "12. Answer Key"),
    ("glossary.html", "Glossary"),
    ("faq.html", "FAQ"),
]

CHAPTER_LABELS = {
    target: label for target, label in TOC_LABELS
}

CSS = """\
:root {
  --bg: #faf8f5; --ink: #2b2b2b; --muted: #6b6560;
  --accent: #8a5a2b; --code-bg: #2d2a26; --code-ink: #f3ede4;
}
* { box-sizing: border-box; }
body {
  margin: 0; background: var(--bg); color: var(--ink);
  font: 18px/1.7 Georgia, 'Times New Roman', serif;
}
.layout { display: flex; max-width: 1200px; margin: 0 auto; }
nav.toc {
  width: 260px; flex-shrink: 0; padding: 2rem 1rem 4rem 1.5rem;
  border-right: 1px solid #e5ded4; position: sticky; top: 0;
  height: 100vh; overflow-y: auto;
}
nav.toc .brand {
  font-weight: bold; font-size: 1.05rem; display: block;
  margin-bottom: 1rem; color: var(--accent);
}
nav.toc a {
  display: block; color: var(--muted); text-decoration: none;
  padding: 0.25rem 0.5rem; border-radius: 6px; font-size: 0.92rem;
}
nav.toc a:hover { background: #f0e9df; color: var(--ink); }
nav.toc a.current { background: #efe4d3; color: var(--accent); font-weight: bold; }
main { flex: 1; min-width: 0; padding: 2.5rem 3rem 5rem 3rem; max-width: 46rem; }
h1, h2, h3 { font-family: 'Helvetica Neue', Arial, sans-serif; line-height: 1.25; }
h1 { font-size: 1.9rem; margin-top: 0.5rem; }
h2 { font-size: 1.35rem; margin-top: 2.4rem; }
h3 { font-size: 1.1rem; margin-top: 2rem; }
p { margin: 1rem 0 1.1rem; }
a { color: var(--accent); }
code {
  font: 0.88em/1.6 ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  background: #efe9df; padding: 0.12em 0.35em; border-radius: 4px;
}
pre {
  background: var(--code-bg); color: var(--code-ink); padding: 1rem 1.2rem;
  border-radius: 10px; overflow-x: auto; margin: 1.2rem 0;
}
pre code { background: none; color: inherit; padding: 0; font-size: 0.85rem; }
blockquote {
  margin: 1.4rem 0; padding: 0.4rem 1.2rem; border-left: 4px solid var(--accent);
  background: #f4ede2; border-radius: 0 8px 8px 0;
}
table {
  border-collapse: collapse; margin: 1.4rem 0; font-size: 0.92rem; width: 100%;
}
th, td { border: 1px solid #e2d9cb; padding: 0.45rem 0.7rem; text-align: left;
  vertical-align: top; }
th { background: #f0e9df; font-family: 'Helvetica Neue', Arial, sans-serif; }
hr { border: none; border-top: 1px solid #e5ded4; margin: 2.5rem 0; }
.pagenav {
  margin-top: 3.5rem; padding-top: 1.4rem; border-top: 1px solid #e5ded4;
  display: flex; justify-content: space-between; gap: 1rem;
  font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 0.95rem;
}
.pagenav a { text-decoration: none; }
footer.credit {
  margin-top: 3rem; color: var(--muted); font-size: 0.85rem;
}
@media (max-width: 860px) {
  .layout { flex-direction: column; }
  nav.toc {
    position: static; width: auto; height: auto; border-right: none;
    border-bottom: 1px solid #e5ded4;
  }
  main { padding: 1.5rem; }
}
"""

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — Terminal Comfort Guide</title>
<style>{css}</style>
</head>
<body>
<div class="layout">
<nav class="toc" aria-label="Table of contents">
<span class="brand">Terminal Comfort Guide</span>
{toc}
</nav>
<main>
{body}
<div class="pagenav">{prevnext}</div>
<footer class="credit">
Terminal Comfort Guide — a local-first, beginner-friendly manual<br>
Built from docs/ with zero dependencies &middot; open source under the MIT License<br>
&copy; 2026 Asdale Dynamics, LLC &middot; <a href="https://dylanasdale.github.io">dylanasdale.github.io</a>
</footer>
</main>
</div>
</body>
</html>
"""


# --------------------------------------------------------------------------
# inline markdown
# --------------------------------------------------------------------------

def convert_inline(text: str) -> str:
    """Inline markdown -> HTML. Protects inline code spans first."""
    pieces = []
    for part in re.split(r"(`[^`]+`)", text):
        if len(part) > 2 and part.startswith("`") and part.endswith("`"):
            pieces.append("<code>" + html.escape(part[1:-1]) + "</code>")
        else:
            pieces.append(html.escape(part))
    text = "".join(pieces)

    def link_convert(match):
        return '<a href="%s">%s</a>' % (
            html.escape(match.group(2), quote=True),
            format_emphasis(match.group(1)),
        )

    text = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link_convert, text)
    return format_emphasis(text)


def format_emphasis(text: str) -> str:
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)
    return text


# --------------------------------------------------------------------------
# block markdown
# --------------------------------------------------------------------------

class BlockParser:
    """Line-based markdown parser. Deliberately small and boring."""

    def __init__(self):
        self.out: list[str] = []
        self.para: list[str] = []
        self.code: list[str] | None = None
        self.list_kind: str | None = None
        self.li_open = False
        self.li_buffer: list[str] = []
        self.quote: list[str] = []
        self.table: list[list[str]] | None = None

    # ---- flush helpers ----
    def flush_para(self):
        if self.para:
            text = convert_inline(" ".join(self.para))
            self.out.append(f"<p>{text}</p>")
            self.para.clear()

    def flush_quote(self):
        if self.quote:
            text = convert_inline(" ".join(self.quote))
            self.out.append(f"<blockquote><p>{text}</p></blockquote>")
            self.quote.clear()

    def flush_table(self):
        if not self.table:
            return
        rows, self.table = self.table, None
        head, rest = rows[0], rows[1:]
        self.out.append("<table><thead><tr>")
        for cell in head:
            self.out.append(f"<th>{convert_inline(cell)}</th>")
        self.out.append("</tr></thead>")
        if rest:
            self.out.append("<tbody>")
            for row in rest:
                self.out.append("<tr>")
                for cell in row:
                    self.out.append(f"<td>{convert_inline(cell)}</td>")
                self.out.append("</tr>")
            self.out.append("</tbody>")
        self.out.append("</table>")

    def close_list(self):
        self.close_li()
        if self.list_kind:
            self.out.append("</ol>" if self.list_kind == "ol" else "</ul>")
            self.list_kind = None

    def close_li(self):
        if self.li_open:
            self.out.append(convert_inline(" ".join(self.li_buffer)) + "</li>")
            self.li_buffer.clear()
            self.li_open = False

    def flush_all(self):
        self.flush_para()
        self.close_list()
        self.flush_quote()
        self.flush_table()

    # ---- one line at a time ----
    def feed(self, raw: str):
        line = raw.rstrip()

        # fenced code block toggles
        if line.startswith("```"):
            if self.code is not None:
                self.out.append(
                    "<pre><code>" + html.escape("\n".join(self.code)) + "</code></pre>"
                )
                self.code = None
            else:
                self.flush_para(); self.close_list(); self.flush_quote(); self.flush_table()
                self.code = []
            return

        if self.code is not None:
            self.code.append(raw)
            return

        stripped = line.strip()

        # blank line: close flow blocks
        if not stripped:
            self.flush_para(); self.close_list(); self.flush_quote(); self.flush_table()
            return

        # horizontal rule
        if re.fullmatch(r"(-{3,}|\*{3,})", stripped):
            self.flush_para(); self.close_list(); self.flush_quote(); self.flush_table()
            self.out.append("<hr>")
            return

        # headings
        match = re.match(r"^(#{1,3})\s+(.*)$", line)
        if match:
            self.flush_all()
            level = len(match.group(1))
            self.out.append(f"<h{level}>" + convert_inline(match.group(2)) + f"</h{level}>")
            return

        # blockquote
        match = re.match(r"^>\s?(.*)$", line)
        if match:
            self.flush_para(); self.close_list(); self.flush_table()
            self.quote.append(match.group(1))
            return

        # table rows (including the |---| separator row)
        if stripped.startswith("|") and stripped.endswith("|"):
            cells = [c.strip() for c in stripped.strip("|").split("|")]
            if self.table is None:
                self.flush_para(); self.close_list(); self.flush_quote()
                self.table = [cells]
            elif len(self.table) == 1 and all(
                re.fullmatch(r":?-+:?", c) for c in cells if c
            ):
                pass  # header separator row: first row already acts as header
            else:
                self.table.append(cells)
            return

        # any non-table line ends a table
        self.flush_table()

        # lists
        match_ul = re.match(r"^\s*[-*]\s+(.*)$", line)
        match_ol = re.match(r"^\s*\d+[.)]\s+(.*)$", line)
        if match_ul or match_ol:
            self.flush_para(); self.flush_quote()
            kind = "ul" if match_ul else "ol"
            if self.list_kind != kind:
                self.close_list()
                self.list_kind = kind
                self.out.append("<ul>" if kind == "ul" else "<ol>")
            else:
                self.close_li()
            self.out.append("<li>")
            content = match_ul.group(1) if match_ul else match_ol.group(1)
            self.li_buffer.append(content)
            self.li_open = True
            return

        # paragraph text (or wrapped list item continuation)
        if self.li_open:
            self.li_buffer.append(stripped)
        else:
            self.para.append(stripped)

    # ---- finish ----
    def result(self) -> str:
        if self.code is not None:  # unterminated fence: still show contents
            self.out.append(
                "<pre><code>" + html.escape("\n".join(self.code)) + "</code></pre>"
            )
            self.code = None
        if self.li_open:
            self.close_li()
        self.flush_all()
        return "\n".join(self.out)


def convert_markdown(md: str) -> str:
    parser = BlockParser()
    for line in md.splitlines():
        parser.feed(line)
    return parser.result()


# --------------------------------------------------------------------------
# page assembly
# --------------------------------------------------------------------------

def extract_title(md: str, fallback: str) -> str:
    for line in md.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def toc_html(current: str) -> str:
    items = []
    for target, label in TOC_LABELS:
        css_class = ' class="current"' if target == current else ""
        items.append(f'<a{css_class} href="{target}">{label}</a>')
    return "\n".join(items)


def prevnext_html(current: str) -> str:
    targets = [target for target, _ in CHAPTERS]
    index = targets.index(current)
    chunks = []
    if index > 0:
        prev_target, prev_label = CHAPTERS[index - 1]
        chunks.append(
            f'<a href="{prev_target}">&larr; {CHAPTER_LABELS[prev_target]}</a>'
        )
    else:
        chunks.append("<span></span>")
    if index < len(targets) - 1:
        nxt_target = targets[index + 1]
        chunks.append(
            f'<a href="{nxt_target}">{CHAPTER_LABELS[nxt_target]} &rarr;</a>'
        )
    else:
        chunks.append("<span></span>")
    return "\n".join(chunks)


def build(out_dir: Path) -> dict:
    out_dir.mkdir(parents=True, exist_ok=True)
    report = {"pages": [], "warnings": []}
    for target, source in CHAPTERS:
        src = DOCS / source
        if not src.exists():
            report["warnings"].append(f"missing source: {src.name}")
            continue
        md = src.read_text(encoding="utf-8")
        page = TEMPLATE.format(
            title=html.escape(extract_title(md, target.removesuffix(".html"))),
            css=CSS,
            toc=toc_html(target),
            body=convert_markdown(md),
            prevnext=prevnext_html(target),
        )
        (out_dir / target).write_text(page, encoding="utf-8")
        report["pages"].append(target)
    return report


def check_links(out_dir: Path) -> list[str]:
    """Return a list of broken internal .html references, if any."""
    if not out_dir.exists():
        return ["no build output found"]
    problems = []
    for page_path in sorted(out_dir.rglob("*.html")):
        page = page_path.read_text(encoding="utf-8")
        for target in re.findall(r'href="([^"#]+\.html)"', page):
            if target.startswith("http"):
                continue
            if not (page_path.parent / target).resolve().exists():
                problems.append(f"{page_path.name} links to missing {target}")
    return problems


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Build the Terminal Comfort Guide site.")
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT, help="output directory")
    parser.add_argument("--check", action="store_true",
                        help="build into a temp dir and verify internal links only")
    args = parser.parse_args(argv)

    if args.check:
        tmp = Path(tempfile.mkdtemp(prefix="tcg-check-"))
        try:
            report = build(tmp)
            problems = check_links(tmp)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
    else:
        if args.out.exists():
            shutil.rmtree(args.out)
        report = build(args.out)
        problems = check_links(args.out)

    for page in report["pages"]:
        print(f"built {page}")
    for warning in report["warnings"]:
        print(f"warning: {warning}", file=sys.stderr)
    for problem in problems:
        print(f"link problem: {problem}", file=sys.stderr)
    if problems or report["warnings"]:
        return 1
    print(f"OK: {len(report['pages'])} pages built, all internal links resolve.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
