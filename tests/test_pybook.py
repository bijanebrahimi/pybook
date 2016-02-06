import os
from unittest import TestCase, main, skip

from pybook import BookConfig

class PyBookConfigTest(TestCase):
    def setUp(self):
        pass

    def test_read_config(self):
        self.config = BookConfig('example')
        self.config.read_config()

        assert self.config.title == "GitBook Example"
        assert self.config.author == "PyBook"
        assert self.config.description == "GitBook Example Description"
        assert self.config.direction == "ltr"
        assert self.config.readme_rel == 'README.md'
        assert self.config.summary_rel == 'SUMMARY.md'

    def test_missing_config(self):
        self.config = BookConfig('example', structure={'book': 'missing-book.json'})
        self.config.read_config()
        assert self.config.readme_rel == 'README.md'

    def test_absolute_path(self):
        self.config = BookConfig('example')
        self.config.read_config()
        assert self.config.readme_abs == os.path.abspath(os.path.join('example/', self.config.readme_rel))
        assert self.config.summary_abs == os.path.abspath(os.path.join('example/', self.config.summary_rel))


if __name__ == '__main__':
    main()
