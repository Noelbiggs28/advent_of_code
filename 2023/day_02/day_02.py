from functools import reduce
def part1():
    in_file = 'output.csv'
    grand_total = 0 
    max_cubes = { 
        "red" : 12,
        "green" : 13,
        "blue" : 14
    }
    with open(in_file, 'r') as infile:
        for line in infile:
            possible_game = True
            stripped_line = line.strip().split(',')
            game_number = stripped_line[0].split(" ")[1]
            for value in stripped_line[1:]:
                # print("value", value)
                cube = value.split(" ") 
                # print("cube", cube)
                if int(cube[1]) > max_cubes[cube[2]]:
                    possible_game = False
                    break
            if possible_game:
                grand_total += int(game_number)
            # print(game_number)
        return grand_total
def part2():
    in_file = 'output.csv'
    grand_total = 0 
    with open(in_file, 'r') as infile:
        for line in infile:
            cubes = {
                "red":0,
                "green":0,
                "blue":0,
            }
            
            stripped_line = line.strip().split(',')
            game_number = stripped_line[0].split(" ")[1]
            for value in stripped_line[1:]:
                
                # print("value", value)
                cube = value.split(" ") 
                # print("cube", cube)
                # cube ['', '2', 'red']
                if int(cube[1]) > cubes[cube[2]]:
                    cubes[cube[2]] = int(cube[1])
            cube_power = reduce(lambda x, y: x * y, cubes.values())
            grand_total += cube_power
       
        return grand_total
print(part1())
print(part2())