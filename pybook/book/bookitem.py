class Chapter:

    def __init__(self, name=None, path=None):
        self.name = name
        self.path = path2
        self.sub_items = []

    def to_json(self):
        pass


class BookItems:

    def __init__(self):
        self.item = None
        self.current_index = 0
        self.stack = []

    def __iter__(self):
        pass
