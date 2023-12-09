from math import prod
# Find the sum of game number of games that are possible
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
            # split them in to "" number cubes
            stripped_line = line.strip().split(',')
            # save game number for later
            game_number = stripped_line[0].split(" ")[1]
            # check cube number against max number
            for value in stripped_line[1:]:
                cube = value.split(" ") 
            # if number > that max break if < then add game number to grandtotal
                if int(cube[1]) > max_cubes[cube[2]]:
                    possible_game = False
                    break
            if possible_game:
                grand_total += int(game_number)
        return grand_total
    
    
# Find the minimum amount of cubes for each game
# Find the product of the cubes
# Find the sum of products
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
            for value in stripped_line[1:]:
                cube = value.split(" ") 
                # cube ['', '2', 'red']
                # store highest number of cubes in a dictionary per color
                if int(cube[1]) > cubes[cube[2]]:
                    cubes[cube[2]] = int(cube[1])
            # multiply number of each color and add em to grand total
            cube_power = prod(cubes.values())
            grand_total += cube_power
       
        return grand_total
print(part1())
print(part2())