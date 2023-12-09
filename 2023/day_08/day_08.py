import time

def part1():
    number_of_steps = 0
    in_file = "input.txt"
    map_dict = {}
    directions = ""
    directions_as_zeros_and_ones = []
    with open(in_file, "r") as infile:
        for _ in infile:
            line = _.strip().split(' = ')

            if line == ['']:
                continue
            if len(line) == 1:
                directions = line[0]
            else:
                conversion = line[1].split(', ')
                first = conversion[0][1:]
                second = conversion[1][:-1]

                map_dict[line[0]] = (first,second) 


    for letter in directions:
        if letter == "L":
            directions_as_zeros_and_ones.append(0)
        else:
            directions_as_zeros_and_ones.append(1)
    current_location = "AAA"
    current_direction = directions_as_zeros_and_ones[0]
    amount_of_directions = len(directions_as_zeros_and_ones)
    while(current_location!="ZZZ"):
        current_location = map_dict[current_location][current_direction]
        number_of_steps +=1
        current_direction =directions_as_zeros_and_ones[number_of_steps%amount_of_directions]
        # time.sleep(3)

    return number_of_steps
print(part1())

def part2():
    number_of_steps = 0
    in_file = "input.txt"
    map_dict = {}
    directions = ""
    directions_as_zeros_and_ones = []
    list_of_starting_points = []
    with open(in_file, "r") as infile:
        for _ in infile:
            line = _.strip().split(' = ')

            if line == ['']:
                continue
            if len(line) == 1:
                directions = line[0]
            else:
                conversion = line[1].split(', ')
                first = conversion[0][1:]
                second = conversion[1][:-1]
                map_dict[line[0]] = (first,second)
                if line[0][2] == "A":
                    list_of_starting_points.append(line[0]) 
    print(list_of_starting_points)
    for letter in directions:
        if letter == "L":
            directions_as_zeros_and_ones.append(0)
        else:
            directions_as_zeros_and_ones.append(1)
    
    current_direction = directions_as_zeros_and_ones[0]
    amount_of_directions = len(directions_as_zeros_and_ones)
    running = True
    while(running):
        still_running = False
        for i, start in enumerate(list_of_starting_points):
            list_of_starting_points[i] = map_dict[start][current_direction]
            if list_of_starting_points[i][2] != "Z":
                still_running = True

        number_of_steps +=1
        current_direction =directions_as_zeros_and_ones[number_of_steps%amount_of_directions]
        if not still_running:
            running = False

        # time.sleep(1)
    return number_of_steps
print(part2())