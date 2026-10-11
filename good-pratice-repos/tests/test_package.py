"""Structural tests for this skill package; no repository or agent is executed.

Run from the package root with:
    python -m unittest discover -s tests -v
Requires Python 3.10+ and only the standard library.
"""
from pathlib import Path
import re
import unittest
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    'SKILL.md', 'README.md',
    'references/baseline.md', 'references/testing.md',
    'references/review.md', 'references/security.md',
    'references/delivery.md', 'references/distribution.md',
    'references/profiles/private.md',
    'references/profiles/open-source.md',
    'references/platforms/github.md',
    'references/platforms/gitlab.md', 'references/sources.md',
    'assets/audit-template.md', 'assets/plan-template.md',
    'assets/repository-contract-template.md',
    'assets/release-checklist.md', 'evals/scenarios.md',
)
LINK = re.compile(r'\[[^\]\n]+\]\(([^)\s]+)\)')


class SkillPackageTests(unittest.TestCase):
    def read_required(self, relative: str) -> str:
        path = ROOT / relative
        self.assertTrue(path.is_file(), f'Missing file: {relative}')
        return path.read_text(encoding='utf-8')

    def test_required_files_exist_and_are_nonempty(self):
        for relative in REQUIRED:
            with self.subTest(file=relative):
                self.assertGreater(len(self.read_required(relative).strip()), 40)

    def test_frontmatter_required_fields_and_name(self):
        text = self.read_required('SKILL.md')
        match = re.match(r'\A---\n(.*?)\n---\n', text, re.S)
        self.assertIsNotNone(match, 'Missing YAML frontmatter delimiters')
        block = match.group(1)
        name = re.search(r'^name: ([a-z0-9-]+)$', block, re.M)
        self.assertIsNotNone(name, 'Missing simple name scalar')
        self.assertEqual(name.group(1), ROOT.name)
        self.assertLessEqual(len(name.group(1)), 64)
        self.assertNotIn('--', name.group(1))
        self.assertFalse(name.group(1).startswith('-'))
        self.assertFalse(name.group(1).endswith('-'))
        description = re.search(r'^description: (.+)$', block, re.M)
        self.assertIsNotNone(description, 'Missing one-line description')
        self.assertTrue(1 <= len(description.group(1)) <= 1024)

    def test_main_instructions_are_bounded(self):
        text = self.read_required('SKILL.md')
        self.assertLess(len(text.splitlines()), 500)
        self.assertLess(len(text.split()), 1900)

    def test_main_routes_to_all_reference_modules(self):
        text = self.read_required('SKILL.md')
        for relative in REQUIRED:
            if relative.startswith('references/'):
                with self.subTest(file=relative):
                    self.assertIn(f']({relative})', text)

    def test_main_routes_to_all_templates(self):
        text = self.read_required('SKILL.md')
        for relative in REQUIRED:
            if relative.startswith('assets/'):
                with self.subTest(file=relative):
                    self.assertIn(f']({relative})', text)

    def test_local_markdown_links_resolve_inside_package(self):
        self.read_required('SKILL.md')
        for path in ROOT.rglob('*.md'):
            for target in LINK.findall(path.read_text(encoding='utf-8')):
                parsed = urlsplit(target)
                if parsed.scheme or parsed.netloc or not parsed.path:
                    continue
                resolved = (path.parent / unquote(parsed.path)).resolve()
                with self.subTest(file=path.relative_to(ROOT), link=target):
                    self.assertTrue(resolved.is_relative_to(ROOT))
                    self.assertTrue(resolved.is_file(), f'Broken link: {target}')

    def test_source_identifiers_exist(self):
        source_text = self.read_required('references/sources.md')
        known = set(re.findall(r'^## (S\d{2})\b', source_text, re.M))
        self.assertGreaterEqual(len(known), 15)
        for path in ROOT.rglob('*.md'):
            for source in re.findall(r'\[(S\d{2})\]', path.read_text(encoding='utf-8')):
                with self.subTest(file=path.relative_to(ROOT), source=source):
                    self.assertIn(source, known)

    def test_only_one_skill_entrypoint(self):
        self.assertEqual(list(ROOT.rglob('SKILL.md')), [ROOT / 'SKILL.md'])

    def test_all_markdown_has_closed_code_fences(self):
        self.read_required('SKILL.md')
        for path in ROOT.rglob('*.md'):
            fences = re.findall(r'^```.*$', path.read_text(encoding='utf-8'), re.M)
            with self.subTest(file=path.relative_to(ROOT)):
                self.assertEqual(len(fences) % 2, 0)

    def test_no_symlinks_or_hidden_direction_controls(self):
        self.read_required('SKILL.md')
        prohibited = set('\u200b\u200c\u200d\u202a\u202b\u202c\u202d\u202e\u2066\u2067\u2068\u2069\ufeff')
        for path in ROOT.rglob('*'):
            self.assertFalse(path.is_symlink(), str(path))
            if path.suffix == '.md':
                with self.subTest(file=path.relative_to(ROOT)):
                    self.assertFalse(prohibited.intersection(path.read_text(encoding='utf-8')))

    def test_behavioral_evaluation_has_explicit_execution_status(self):
        text = self.read_required('evals/scenarios.md')
        self.assertIn('NÃO EXECUTADO', text)
        self.assertGreaterEqual(len(re.findall(r'^## E\d{2}\b', text, re.M)), 10)
        self.assertIn('Critério de reprovação', text)


if __name__ == '__main__':
    unittest.main()
