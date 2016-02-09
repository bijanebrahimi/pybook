import os
from unittest import TestCase, main, skip
from datetime import datetime

from pybook import Book
from pybook import BookConfig
from pybook.utils import BookError

file_path = os.path.dirname(__file__)
test_path = os.path.join(file_path, 'example')

class BookConfigTest(TestCase):
    def setUp(self):
        pass

    def test_read_config(self):
        self.config = BookConfig(test_path)
        self.config.read_config()

        assert self.config.title == "GitBook Example"
        assert self.config.author == "PyBook"
        assert self.config.description == "GitBook Example Description"
        assert self.config.direction == "ltr"
        assert self.config.readme_rel == 'README.md'
        assert self.config.summary_rel == 'SUMMARY.md'

    def test_missing_config(self):
        self.config = BookConfig(test_path, structure={'book': 'missing-book.json'})
        self.config.read_config()
        assert self.config.readme_rel == 'README.md'

    def test_absolute_path(self):
        self.config = BookConfig(test_path)
        self.config.read_config()

        print(self.config.readme_abs, os.path.join(test_path, self.config.readme_rel))
        assert self.config.readme_abs == os.path.join(test_path, self.config.readme_rel)
        assert self.config.summary_abs == os.path.join(test_path, self.config.summary_rel)


if __name__ == '__main__':
    main()
