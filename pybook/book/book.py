import os

from .bookconfig import BookConfig
from pybook.parse.summary import construct_bookitems
from pybook.utils import logger


class Book:
    def __init__(self, root, build='build', **book_config):
        self.config = BookConfig(root=root, build=build, **book_config)
        self.chapters = []

        self.renderers = {}

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
        self.read_summary()
        self.create_chapters()
        logger.info('Initialization Finished')

    def create_chapters(self, chapters=None):
        if not chapters:
            chapters = self.chapters
        for chapter in chapters:
            chapter_dir = os.path.dirname(chapter.path)
            if not os.path.exists(chapter_dir):
                logger.info('Creating %s' % chapter_dir)
                os.mkdir(chapter_dir)
            if not os.path.exists(chapter.path):
                logger.info('Creating %s' % chapter.path)
                with open(chapter.path, 'w') as f:
                    f.write("# %s\n\n" % chapter.name)
                    f.write("Content goes here.\n")
            if chapter.articles:
                self.create_chapters(chapter.articles)

    def build(self):
        logger.info('Start Building ...')
        self.read_config_and_summary()
        for (name, renderer) in self.renderers.items():
            renderer.render()
        logger.info('Building is Finished')

    def read_config(self):
        self.config.read_config()

    def read_config_and_summary(self):
        self.read_config()
        summary_path = self.config.summary_abs
        self.chapters = construct_bookitems(summary_path)

    def read_summary(self):
        summary_path = self.config.summary_abs
        self.chapters = construct_bookitems(summary_path)

    @property
    def summary(self):
        return self.chapters
