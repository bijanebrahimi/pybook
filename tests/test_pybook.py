import os
from unittest import TestCase, main, skip

from pybook import BookConfig

class PyBookConfigTest(TestCase):
    def setUp(self):
        self.config = BookConfig('example')

    def test_read_config(self):
        self.config.read_config()

        assert self.config.title == "GitBook Example"
        assert self.config.author == "PyBook"
        assert self.config.description == "GitBook Example Description"
        assert self.config.direction == "ltr"


if __name__ == '__main__':
    main()
