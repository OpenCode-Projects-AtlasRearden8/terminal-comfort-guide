"""Tests for the Terminal Comfort Guide.

Run with:  python3 -m unittest discover -s tests -v
(Standard library only — no test packages to install.)
"""

import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "engine"))
import build  # noqa: E402


class TestMarkdownConverter(unittest.TestCase):
    def convert(self, md: str) -> str:
        return build.convert_markdown(md)

    def test_heading_levels(self):
        html = self.convert("# One\n## Two\n### Three")
        self.assertIn("<h1>One</h1>", html)
        self.assertIn("<h2>Two</h2>", html)
        self.assertIn("<h3>Three</h3>", html)

    def test_fenced_code_block_escapes_and_preserves(self):
        html = self.convert("text ```\nPS C:\\Users>You>\n```")
        self.assertIn("<pre><code>", html)
        self.assertIn("PS C:\\Users&gt;You&gt;", html)

    def test_inline_code_and_bold(self):
        html = self.convert("run **bold** and `code`")
        self.assertIn("<strong>bold</strong>", html)
        self.assertIn("<code>code</code>", html)

    def test_bold_bold(self):
        html = self.convert("**whole bold** with *italics* mid")
        self.assertIn("<strong>whole bold</strong>", html)
        self.assertIn("<em>italics</em>", html)

    def test_paragraph_wrap_joining_no_hard_break(self):
        html = self.convert("alpha bravo\ncharlie delta done")
        self.assertIn("alpha bravo charlie delta done", html)
        self.assertNotIn("<br>", html)

    def test_bullet_list_items_are_separate(self):
        html = self.convert("- one\n- two\n- three")
        self.assertEqual(html.count("<li>"), 3)
        self.assertEqual(html.count("</li>"), 3)
        self.assertIn("<ul>", html)

    def test_ordered_list_items_are_separate(self):
        html = self.convert("1. first\n2. second\n3. third with wrap\n   extra text")
        self.assertEqual(html.count("<li>"), 3)
        self.assertIn("first", html)
        self.assertIn("second", html)
        self.assertIn("third with wrap extra text", html)

    def test_blockquote(self):
        html = self.convert("> a calm note\n> across two lines")
        self.assertIn("<blockquote><p>a calm note across two lines</p></blockquote>", html)

    def test_table_renders_with_header_and_rows(self):
        html = self.convert(
            "| A | B |\n| --- | --- |\n| a1 | b1 |\n| a2 | b2 |"
        )
        self.assertIn("<th>A</th>", html)
        self.assertIn("<th>B</th>", html)
        self.assertIn("<td>a1</td>", html)
        self.assertIn("<td>b2</td>", html)
        self.assertNotIn("---", html)

    def test_horizontal_rule(self):
        html = self.convert("before\n\n---\n\nafter")
        self.assertIn("<hr>", html)

    def test_link(self):
        html = self.convert("see [Chapter 2](ch-02-moving-around.html)")
        self.assertIn('<a href="ch-02-moving-around.html">Chapter 2</a>', html)

    def test_html_is_escaped_in_prose(self):
        html = self.convert("a < b & c > d")
        self.assertIn("a &lt; b &amp; c &gt; d", html)


class TestBuiltSite(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory(prefix="tcg-tests-")
        cls.out = Path(cls.tmp.name) / "site"
        cls.report = build.build(cls.out)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_all_chapter_sources_exist(self):
        for target, source in build.CHAPTERS:
            self.assertTrue((build.DOCS / source).exists(), f"missing {source}")

    def test_every_documented_page_is_built(self):
        built = set(self.report["pages"])
        expected = {target for target, _ in build.CHAPTERS}
        self.assertEqual(built, expected)
        self.assertFalse(self.report["warnings"])

    def test_no_broken_internal_links(self):
        self.assertEqual(build.check_links(self.out), [])

    def test_index_is_welcome_page(self):
        html = (self.out / "index.html").read_text(encoding="utf-8")
        self.assertIn("Read Me First, Friend", html)

    def test_every_page_carries_the_credit(self):
        for page in self.out.glob("*.html"):
            text = page.read_text(encoding="utf-8")
            self.assertIn("2026 Asdale Dynamics, LLC", text)
            self.assertIn("MIT License", text)

    def test_exercises_and_answer_key_present(self):
        exercises = (self.out / "ch-11-exercises.html").read_text(encoding="utf-8")
        key = (self.out / "ch-12-answer-key.html").read_text(encoding="utf-8")
        self.assertIn("Ten exercises", exercises)
        self.assertEqual(
            # exercises count headings "### Exercise/ Bonus"
            len(re.findall(r"<h3>", exercises)),
            11,
        )
        self.assertIn("Answer Key", key)

    def test_glossary_table_has_entries(self):
        gloss = (self.out / "glossary.html").read_text(encoding="utf-8")
        self.assertGreaterEqual(gloss.count("<tr>"), 20)

    def test_code_samples_survive(self):
        ollama = (self.out / "ch-05-ollama.html").read_text(encoding="utf-8")
        self.assertIn("ollama run llama3.2:1b", ollama)


class TestHelloScript(unittest.TestCase):
    def test_script_runs_and_is_friendly(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "hello_local_ai.py")],
            capture_output=True,
            text=True,
            timeout=60,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Hello! This is your first script", result.stdout)
        self.assertIn("Python version is:", result.stdout)
        self.assertIn("install once, list what you have", result.stdout)


class TestBuildCheckCommand(unittest.TestCase):
    def test_check_mode_exits_zero_with_viable_output(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "engine" / "build.py"), "--check"],
            capture_output=True,
            text=True,
            timeout=120,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("OK:", result.stdout)


if __name__ == "__main__":
    unittest.main()
