import os
from datetime import datetime
from pybook.utils import logger
from .bookconfig import BookConfig


class BookItem:
    def __init__(self, root):
        self.set_root(root)

    def set_root(self, root):
        self.root = root

    @property
    def content(self):
        file_path = os.path.join(self.root, self.path)
        print(file_path)
        with open(file_path) as f:
            return f.read()

    @property
    def mtime(self):
        file_path = os.path.join(self.root, self.path)
        try:
            return datetime.fromtimestamp(os.path.getmtime(file_path))
        except OSError:
            return None


class Affix(BookItem):
    def __init__(self, root=None, title=None, path=None):
        super(Affix, self).__init__(root=root)
        self.title = title
        self.path = path

    def __repr__(self):
        return "Affix(%s, %s)" % (self.title, self.path)


class Chapter(BookItem):
    def __init__(self, root=None, title=None, path=None):
        super(Chapter, self).__init__(root=root)
        self.title = title
        self.path = path
        self.articles = []

    def __repr__(self):
        return "Chapter(%s, %s)" % (self.title, self.path)
