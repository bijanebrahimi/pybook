import os

from pybook.utils import logger
from .bookconfig import BookConfig


class BookItem:
    pass


class Affix(BookItem):
    def __init__(self, name=None, path=None):
        super(Chapter, self).__init__()
        self.name = name
        self.path = path

    def __repr__(self):
        return "Affix(%s, %s)" % (self.name, self.path)


class Chapter(BookItem):
    def __init__(self, name=None, path=None):
        super(Chapter, self).__init__()
        self.name = name
        self.path = path
        self.articles = []

    def __repr__(self):
        return "Chapter(%s, %s)" % (self.name, self.path)
