from folder import Folder

class Computer:
    def __init__(self):
        self.all_folder = []
        self.home = Folder('home', 'at top')
        self.outer_most_folder = self.home
    