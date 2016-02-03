import os

from pybook.book.bookitem import BookItem, BookItems
from pybook.book.bookconfig import BookConfig
from pybook.parse.summary import construct_bookitems
from pybook.utils import logger

class PyBook:
    def __init__(self, root, build='build'):
        self.config = BookConfig(root=root, build=build)
        self.book_items = []
        self.renderers = []
        # TODO: set default renderers

    def init(self):
        logger.info('Start Initializing ...')
        if not os.path.exists(self.config.root):
            logger.info('Creating Root Directory')
            os.mkdir(self.config.root)

        if not os.path.exists(self.config.build):
            logger.info('Creating Build Directory')
            os.mkdir(self.config.build)

        if not os.path.exists(self.config.summary_abs):
            with open(self.config.summary_abs, 'w') as f:
                f.write('# Summary\n')
                f.write('\n')
                f.write('- [Chapter 1](./chapter_1/readme.md)\n')

        self.parse_summary()
        # TODO: iter through contets and create chapter files
        self.__create_nodes()
        logger.info('Initialization Finished')

    def __create_nodes(self, chapters=None):
        if not chapters:
            chapters = self.book_items
        for chapter in chapters:
            chapter_dir = os.path.dirname(chapter.path)
            if not os.path.exists(chapter_dir):
                logger.info('Creating %s' % chapter_dir)
                os.mkdir(chapter_dir)
            if not os.path.exists(chapter.path):
                logger.info('Creating %s' % chapter.path)
                os.mknod(chapter.path)
            if chapter.sub_items:
                self.__create_nodes(chapter.sub_items)

    def build(self):
        pass

    def read_config(self):
        self.config.read_config()

    def parse_summary(self):
        summary_path = self.config.summary
        self.book_items = construct_bookitems(summary_path)
