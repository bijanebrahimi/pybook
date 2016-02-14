import os
from secretary import Renderer as Secretary
from pybook.utils import logger


class Renderer:
    def __init__(self):
        pass


class ODTRenderer(Renderer):
    def __init__(self, book, template, destination, filters=None):
        if not filters:
            filters = {}
        self.set_template(template)
        self.book = book
        self.set_destination(destination)
        self.engine = Secretary(markdown_extras=['fenced-code-blocks',
                                                 'footnotes',
                                                 'tables'])
        self.engine.environment.filters.update(filters)

    def set_template(self, template):
        if not os.path.isabs(template):
            current_path = os.path.dirname(os.path.abspath(__file__))
            template = os.path.join(current_path, template)
        self.template = template

    def set_destination(self, destination):
        if not os.path.exists(destination):
            os.makedirs(destination)
        self.destination = destination

    def render(self):
        logger.debug('ODT Renderer Initialized')
        book_title = self.book.config.title or 'book'
        book_name = '%s.odt' % book_title
        book_path = os.path.join(self.destination, book_name)

        logger.debug(self.book.summary[0].content)
        result = self.engine.render(self.template,
                                    book=self.book,
                                    **self.book.config.variables)
        with open(book_path, 'wb') as f:
            f.write(result)
        logger.debug('ODT Renderer Finished')
        return True
