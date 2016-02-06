import os
from unittest import TestCase, main, skip

from pybook.parse.summary import *

class PyBookParseTest(TestCase):
    def setUp(self):
        pass

    def test_level(self):
        assert parse_level('- Top Level Item') == 0
        assert parse_level('    - Second Level Item') == 1
        assert parse_level('        - Third Level Item') == 2
        assert parse_level('    - Third Level Item', spaces_in_tab=2) == 2

    def test_parse_line(self):
        ch = parse_line('  - [Chapter 1](./chapter_01.md)')
        assert ch.name == "Chapter 1"
        assert ch.path == "./chapter_01.md"

    def test_parse_level(self):
        lines = ('- [Chapter 1](./chapter_01.md)\n'
                 '    - [Chapter 1.1](./chapter_01_1.md)\n'
                 '- [Chapter 2](./chapter_02.md)\n')
        chapters = parse_levels(lines.split('\n'), current_level=0)
        assert len(chapters) == 2


if __name__ == '__main__':
    main()
