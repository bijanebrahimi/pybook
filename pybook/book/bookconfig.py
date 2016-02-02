import os
import yaml

class BookConfig(Object):

    def __init__(self):
        title = None
        author = None
        root = None
        src = None
        dst = None
        multilingual = False

    def read_config(self):
        try:
            with open('book.json') as bookjson:
                config_file = yaml.load(stream.read())
        except:
            # TODO: check for different exceptions
            return self

        self.title = config_file.get('title', '').strip()
        self.author = config_file.get('author', '').strip()
        self.dest = os.path.abspath('.')

    def get_root(self):
        return self.root

    def set_root(self, root):
        self.root = root
        return self

    def get_src(self):
        return self.src

    def set_src(self, src):
        self.src = src
        return self

    def get_dest(self):
        return self.dest

    def set_dest(self, dest):
        self.dest = dest
        return self
