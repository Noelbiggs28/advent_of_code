class Folder:
    def __init__(self, name, parent):
        self.parent_folder = parent
        self.name = name
        self.contents = []