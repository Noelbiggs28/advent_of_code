# If numbers touch a symbol they are a part number
# Find the sum of part numbers
# Example = 4361



def part1():
    visual = []
    unique_symbols = "-@*=%/$#+&"
    in_file = "input.txt"
    with open(in_file, "r") as infile:
        for line in infile:
            line = line.strip()
            visual.append([line])

# make a dictionary with all the coords adjacent to the parts
    all_coords_adj_parts = {} 
    for y in range(len(visual)):
        for x in range(len(visual[y][0])):
            spot = visual[y][0][x]
            if spot.isdigit() :
                continue
            elif spot in unique_symbols:
                all_coords_adj_parts[(y+1,x)]=True
                all_coords_adj_parts[(y-1,x)]=True
                all_coords_adj_parts[(y,x+1)]=True
                all_coords_adj_parts[(y,x-1)]=True
                all_coords_adj_parts[(y+1,x+1)]=True
                all_coords_adj_parts[(y+1,x-1)]=True
                all_coords_adj_parts[(y-1,x+1)]=True
                all_coords_adj_parts[(y-1,x-1)]=True



    part_number_total = 0
    for y in range(len(visual)):
        # current part number being built
        part_number = ""
        part_adj_number = False
        for x in range(len(visual[y][0])):
            spot = visual[y][0][x]
            # if it is a digit add it to the part number
            if spot.isdigit():
                part_number+=spot
                # check if next to part
                if (y,x) in all_coords_adj_parts:
                    part_adj_number = True
                # if its the end of a line. add the part number to total if next to part and reset
                if int(x) == len(visual[y][0])-1:
                    if part_adj_number:
                        part_number_total += int(part_number)
                        part_number = ''
                        part_adj_number = False
            # if its not a digit and the part number is not empty add it to the total and reset
            else:
                if len(part_number)>0:
                    if part_adj_number == True:
                        part_number_total+=int(part_number)
                    part_number = ''
                    part_adj_number = False
    # [
    # ['467..114..'], 
    # ['...*......'], 
    # ['..35..633.'], 
    # ['......#...'], 
    # ['617*......'], 
    # ['.....+.58.'], 
    # ['..592.....'], 
    # ['......755.'], 
    # ['...$.*....'], 
    # ['.664.598..']]

    return part_number_total
print(part1())
# 529539 too low


# 467835 example answer
def part2():
    visual = []
    in_file = "input.txt"
    with open(in_file, "r") as infile:
        for line in infile:
            line = line.strip()
            visual.append([line])

# make a dictionary with all the coords adjacent to the parts
    all_coords_adj_gear = {} 
    gear_coords = {}
    for y in range(len(visual)):
        for x in range(len(visual[y][0])):
            spot = visual[y][0][x]
            if spot.isdigit() :
                continue
            elif spot == "*":
                gear_coords[y,x] = []
                all_coords_adj_gear[(y+1,x)]=(y,x)
                all_coords_adj_gear[(y-1,x)]=(y,x)
                all_coords_adj_gear[(y,x+1)]=(y,x)
                all_coords_adj_gear[(y,x-1)]=(y,x)
                all_coords_adj_gear[(y+1,x+1)]=(y,x)
                all_coords_adj_gear[(y+1,x-1)]=(y,x)
                all_coords_adj_gear[(y-1,x+1)]=(y,x)
                all_coords_adj_gear[(y-1,x-1)]=(y,x)


    
    for y in range(len(visual)):
        # current part number being built
        part_number = ""
        gear_adj_number = False
        for x in range(len(visual[y][0])):
            spot = visual[y][0][x]
            # if it is a digit add it to the part number
            if spot.isdigit():
                part_number+=spot
                # check if next to part
                if (y,x) in all_coords_adj_gear:
                    gear_adj_number = all_coords_adj_gear[(y,x)]
                    print(gear_adj_number)
                # if its the end of a line. add the part number to total if next to part and reset
                if int(x) == len(visual[y][0])-1:
                    if gear_adj_number:
                        gear_coords[gear_adj_number].append(part_number)
                        part_number = ''
                        gear_adj_number = False
            # if its not a digit and the part number is not empty add it to the total and reset
            else:
                if len(part_number)>0:
                    if gear_adj_number:
                        gear_coords[gear_adj_number].append(part_number)
                    part_number = ''
                    gear_adj_number = False
    filtered_values = [value for value in gear_coords.values() if len(value) == 2]
    products = [int(value[0])*int(value[1]) for value in filtered_values]
    return sum(products)

print(part2())
