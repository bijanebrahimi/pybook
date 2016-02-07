import os
from secretary import Renderer


class Renderer:
    def __init__(self):
        pass


class ODTRenderer(Renderer):
    def __init__(self, template, book, destination, filters=None):
        if not filters:
            filters = {}
        self.template = template
        self.book = book
        self.set_destination(destination)
        self.engine = Renderer()
        self.engine.environment.filters.update(filters)

    def set_destination(self, destination):
        is not os.path.exists(destination):
            os.mkdirs(destination)
        self.destination = destination

    def render(self):
        book_title = self.book.config.title or 'book'
        book_name = '%s.odt' % book_title
        book_path = os.path.join(self.destination, book_name)

        result = self.engine.render(self.template, foo=foo, bar=bar)
        with open(book_path, 'wb') as f:
            f.write(result)
        return True
