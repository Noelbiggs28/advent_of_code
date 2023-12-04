class Knot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.tail_spot = []

    def move(self, head):
        if head.x - 2 == self.x:
            self.x +=1
            if head.y < self.y:
                 self.y -=1
            elif head.y > self.y:
                 self.y +=1

        elif head.x + 2 == self.x:
            self.x -= 1
            if head.y < self.y:
                self.y -= 1
            elif head.y > self.y:
                self.y += 1

        elif head.y - 2 == self.y:
            self.y += 1
            if head.x < self.x:
                self.x -=1
            elif head.x > self.x:
                self.x +=1

        elif head.y + 2 == self.y:
            self.y -=1
            if head.x < self.x:
                self.x -=1
            elif head.x > self.x:
                self.x +=1

    def add_spot(self):
        if [self.x, self.y] not in self.tail_spot:
            self.tail_spot.append([self.x,self.y])