import os


class BookItem:
    pass


class Chapter(BookItem):
    def __init__(self, name=None, path=None):
        super(Chapter, self).__init__()
        self.name = name
        self.path = path
        self.sub_items = []

    def to_json(self):
        pass

    def __repr__(self):
        return "Chapter(%s, %s)" % (self.name, self.path)


class BookItems:
    def __init__(self, items=None):
        self.items = items if items else []

    def iter(self, items=None):
        if not items:
            items = self.items
        for item in items:
            yield item
            for sub_item in self.iter(items=item.sub_items):
                yield sub_item
