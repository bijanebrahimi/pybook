import os

from pybook.book.bookitem import BookItem, BookItems
from pybook.book.bookconfig import BookConfig
from pybook.parse.summary import construct_bookitems
from pybook.renderers import HtmlRenderer
from pybook.utils import logger

class PyBook:
    def __init__(self, root, build='build'):
        self.config = BookConfig(root=root, build=build)
        self.book_items = []

        html_renderer = HtmlRenderer(self)
        self.renderers = {'html': html_renderer}

    def init(self):
        logger.info('Start Initializing ...')
        self.read_config()
        if not os.path.exists(self.config.root):
            logger.info('Creating Root Directory')
            os.mkdir(self.config.root)

        if not os.path.exists(self.config.build):
            logger.info('Creating Build Directory')
            os.mkdir(self.config.build)

        if not os.path.exists(self.config.summary_abs):
            logger.debug("Creating Default SUMMARY.md")
            with open(self.config.summary_abs, 'w') as f:
                f.write('# Summary\n')
                f.write('\n')
                f.write('- [Introduction](./chapter_1/intro.md)\n')
                f.write('    - [Who this book is for](./chapter_1/1_1.md)\n')
                f.write('- [Chapter 1](./chapter_2/Usage.md)\n')

        self.__parse_summary()
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
        logger.info('Start Building ...')
        self.read_config()
        self.__parse_summary()
        for (name, renderer) in self.renderers.items():
            renderer.render()
        logger.info('Building is Finished')

    def read_config(self):
        self.config.read_config()

    def __parse_summary(self):
        summary_path = self.config.summary_abs
        self.book_items = construct_bookitems(summary_path)
