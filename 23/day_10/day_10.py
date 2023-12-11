# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.


def check_adj_squares(original_map, current_square, tracker_map, steps):
    max_y = len(original_map)-1
    max_x = len(original_map[0])-1
    if current_square[0] < max_y:
        print(current_square)
        next_spot = original_map[current_square[0]+1][current_square[1]]
        if next_spot in ["|", "J", "L"]:
            steps +=1
            tracker_map[current_square[0]+1][current_square[1]] = steps
            if next_spot == "|":
                steps +=1
                tracker_map[current_square[0] + 2][current_square[1]] = steps
                check_adj_squares(original_map, [current_square[0] + 2, current_square[1]], tracker_map, steps)
            elif next_spot == "L":
                check_adj_squares(original_map, [current_square[0] + 1, current_square[1] + 1], tracker_map, steps)
            elif next_spot == "J":
                check_adj_squares(original_map, [current_square[0] + 1, current_square[1] - 1], tracker_map, steps)




def part1(in_file):
    original_map = []
    furthest_distance = 0
    y = 0
    x = 0
    starting_spot = None
    with open(in_file,"r") as infile:
        for _ in infile:
            x = 0
            line = _.strip()
            original_map.append(list(line))
            for spot in line:
                if spot == "S":
                    starting_spot = [y,x]
                x += 1
            y += 1
    print(original_map)
    tracker_map = [line for line in original_map]
    steps = 0
    check_adj_squares(original_map, starting_spot, tracker_map, steps)
    print(tracker_map)



    return furthest_distance
print(part1("example.txt"))