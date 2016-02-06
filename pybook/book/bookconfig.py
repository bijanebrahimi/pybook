import os
import json

from pybook.utils import logger


class BookConfig:
    def __init__(self, root, build='build'):
        self.title = None
        self.author = None
        self.description = None
        self.variables = {}
        self.structure = {'readme': 'README.md',
                          'summary': 'SUMMARY.md'}
        self.language = 'en'
        self.direction = 'ltr'
        self.set_root(root)
        self.set_build(build)

    def set_root(self, root):
        if not os.path.isabs(root):
            root = os.path.abspath(root)
        self.root = root

    def set_build(self, build):
        if not os.path.isabs(build):
            root = os.path.join(self.root, build)
        self.build = build

    def read_config(self):
        try:
            config_path = os.path.join(os.path.abspath(self.root), 'book.json')
            logger.debug('Reading book.json')
            with open(config_path, 'r') as config_file:
                book_json = json.loads(config_file.read())
        except FileNotFoundError as e:
            logger.debug('Cannot find book.json File')
            return
        except Exception as e:
            # TODO: raise Exception as this should not happen
            logger.debug('Error Reading book.json File')
            return

        self.title = book_json.get('title', '').strip()
        self.author = book_json.get('author', '').strip()
        self.description = book_json.get('description', '').strip()
        self.language = book_json.get('language', 'en').strip()
        self.direction = book_json.get('direction', 'ltr').strip()
        self.variables = book_json.get('variables', {})
        self.structure.update(book_json.get('structure', {}))

    @property
    def summary_rel(self):
        return self.structure['summary']

    @property
    def summary_abs(self):
        return os.path.join(self.root, self.summary_rel)

    @property
    def readme_rel(self):
        return self.structure['readme']

    @property
    def readme_abs(self):
        return ps.path.join(self.root, self.readme_rel)
