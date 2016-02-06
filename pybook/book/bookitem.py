import os


class BookItem:
    pass


class Chapter(BookItem):
    def __init__(self, name=None, path=None):
        super(Chapter, self).__init__()
        self.name = name
        self.path = path
        self.articles = []

    def __repr__(self):
        return "Chapter(%s, %s)" % (self.name, self.path)


class BookItems:
    def __init__(self, items=None):
        self.items = items if items else []

    def iter(self, articles=None):
        if not articles:
            articles = self.articles
        for article in articles:
            yield article
            for sub_articles in self.iter(items=item.articles):
                yield sub_articles
