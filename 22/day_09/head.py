class Head:
    def __init__(self):
        self.x = 0
        self.y = 0

    def move(self, letter):
        if letter == "R":
            self.x += 1
        elif letter == "L":
            self.x -= 1
        elif letter == "U":
            self.y += 1
        else:
            self.y -= 1
