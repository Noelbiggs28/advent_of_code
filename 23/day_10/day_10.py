# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
def part1(in_file):
    furthest_distance = 0
    with open(in_file,"r") as infile:
        for _ in infile:
            line = _.strip()
            print(line)
    return furthest_distance
print(part1("example.txt"))