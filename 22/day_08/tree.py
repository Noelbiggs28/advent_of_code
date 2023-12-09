class Tree():
    def __init__(self, height, y , x):
        
        self.name = f'{y}{x}'
        self.height = int(height)
        self.x_coord = x
        self.y_coord = y
        self.spotted = False
        self.scenic_score = 0

    def rec_left(self, y, x, tree_map):
        score = 0
        if x == 0:
            return 0
        elif tree_map[y][x-1].height >= self.height:
            return 1
        else:
            score += 1
            score += self.rec_left(y,x-1, tree_map)
        return score
        
    def rec_right(self, y, x, tree_map):
        score = 0
        if x == len(tree_map[0])-1:
            return 0
        elif tree_map[y][x+1].height >= self.height:
            return 1
        else:
            score += 1
            score += self.rec_right(y,x+1, tree_map)
        return score

    def rec_up(self, y, x, tree_map):
        score = 0
        if y == 0:
            return 0
        elif tree_map[y-1][x].height >= self.height:
            return 1
        else:
            score += 1
            score += self.rec_up(y-1, x, tree_map)
        return score
    
    def rec_down(self, y, x, tree_map):
        score = 0
        if y == len(tree_map)-1:
            return 0
        elif tree_map[y+1][x].height >= self.height:
            return 1
        else:
            score += 1
            score += self.rec_down(y+1,x, tree_map)
        return score
