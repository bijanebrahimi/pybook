import os
import json

from pybook.utils import logger


class BookConfig:
    def __init__(self, root):
        self.title = None
        self.author = None
        self.description = None
        self.variables = {}
        self.root = root
        self.build = None
        self.multilingual = False

    def read_config(self):
        try:
            config_path = os.path.join(os.path.abspath(self.root), 'book.json')
            logger.debug('Reading `%s`' % config_path)
            with open(config_path, 'r') as book_file:
                book_json = json.loads(book_file.read())
        except FileNotFoundError as e:
            logger.debug('Cannot find `book.json`')
            return
        except Exception as e:
            logger.debug('Error reading %s' % config_path)
            return

        self.title = book_json.get('title', '').strip()
        self.author = book_json.get('author', '').strip()
        self.description = book_json.get('description', '').strip()
        self.direction = book_json.get('direction', '').strip()
        self.variables = book_json.get('variables', {})

        self.build = os.path.abspath('build')
        return self
