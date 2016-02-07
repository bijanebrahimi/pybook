import os
from unittest import TestCase, main, skip
from datetime import datetime

from pybook import Book
from pybook import BookConfig
from pybook.utils import BookError

class BookConfigTest(TestCase):
    def setUp(self):
        pass

    @skip
    def test_summary_syntax_error(self):
        book = Book('example', structure={'summary': 'BAD_INDENTATION_SUMMARY.md'})
        book.read_config()
        assert book.config.summary_rel == 'BAD_INDENTATION_SUMMARY.md'
        self.assertRaises(BookError, book.init)

    @skip
    def test_summary(self):
        book = Book('example')
        book.read_config_and_summary()
        assert len(book.summary) == 1
        introduction = book.summary[0]
        assert isinstance(introduction.mtime, datetime) == True
        assert isinstance(introduction.content, str) == True

if __name__ == '__main__':
    main()
