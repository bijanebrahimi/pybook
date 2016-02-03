import os

from pybook.book.bookitem import BookItem, BookItems
from pybook.book.bookconfig import BookConfig
from pybook.parse.summary import construct_bookitems
from pybook.utils import logger

class PyBook:
    def __init__(self, root_path):
        self.config = None
        self.book_items = []
        self.renderers = []
        if not os.path.isabs(root_path):
            root_path = os.path.abspath(root_path)

        build_path = os.path.join(root_path, 'build')
        self.config = BookConfig(root_path)
        self.set_build(build_path)
        # TODO: set default renderers
        pass

    def init(self):
        logger.debug('Init ...')
        root_path = self.config.root
        if not os.path.exists(root_path):
            logger.debug('Creating Root Directory: %s' % root_path)
            os.mkdir(self.root_path)

        build_path = self.config.build
        if not os.path.exists(build_path):
            logger.debug('Creating Build Directory: %s' % build_path)
            os.mkdir(build_path)

        summary_path = os.path.join(root_path, 'SUMMARY.md')
        if not os.path.exists(summary_path):
            with open(summary_path, 'w') as f:
                f.write('# Summary\n')
                f.write('\n')
                f.write('- [Chapter 1](./chapter_1/readme.md)\n')
                # TODO: remove this, just for debugging
                f.write('    - [Chapter 1.1](./chapter_1/1.md)\n')
                f.write('- [Chapter 2](./chapter_2/readme.md)\n')

        # TODO: iter through contets and create chapter files
        self.parse_summary()
        self.__create_chapters_files()
        logger.debug('Init Done')

    def __create_chapters_files(self, chapters=None):
        if not chapters:
            chapters = self.book_items
        for chapter in chapters:
            chapter_dir = os.path.dirname(chapter.path)
            if not os.path.exists(chapter_dir):
                logger.debug('Creating %s' % chapter_dir)
                os.mkdir(chapter_dir)
            if not os.path.exists(chapter.path):
                logger.debug('Creating %s' % chapter.path)
                os.mknod(chapter.path)
            if chapter.sub_items:
                self.__create_chapters_files(chapter.sub_items)

    def build(self):
        pass

    def read_config(self):
        self.config.read_config()

    def set_root(self, root):
        self.config.root = root

    def get_root(self):
        return self.config.root

    def set_build(self, build):
        self.config.build = build

    def get_build(self):
        return self.config.build

    def parse_summary(self):
        summary_path = os.path.join(self.get_root(), 'SUMMARY.md')
        self.book_items = construct_bookitems(summary_path)
