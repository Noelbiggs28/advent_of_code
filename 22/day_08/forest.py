from tree import Tree
class Forest:
    def __init__(self):
        self.rows =[]
        self.columns = []

    def add_line_to_rows(self, line):
        self.rows.append(line)

    def add_line_to_col(self, line):
        self.columns.append(line)

    def get_dimensions(self, file):
        x = 0
        y = 0
        with open(file,'r') as infile:
            for line in infile:
                line = line.strip()
                for _ in line:
                    if y == 0:
                        x += 1
                y += 1
        return [x,y]
    
    def make_empty_forest(self, list):
        x = list[0]
        y = list[1]
        empty_forest = []
        for _ in range(x):
            row = []
            for _ in range(y):
                row.append('_')
            empty_forest.append(row)
        return empty_forest
    
    def fill_with_trees(self, file, dashes):
        with open(file,'r') as infile:
            y = 0
            for line in infile:
                line = line.strip()
                x = 0
                for num in line:
                    dashes[y][x] = Tree(num, y, x)
                    x+=1
                y += 1
        return dashes
    
    def fill_with_heights(self, file, dashes):
        with open(file, 'r') as infile:
            y = 0
            for line in infile:
                line = line.strip()
                x = 0
                for num in line:
                    dashes[x][y] = num
                    x+=1
                y+=1
        return dashes
            