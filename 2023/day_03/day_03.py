
# If numbers touch a symbol they are a part number
# Find the sum of part numbers
# Example = 4361
def part1():
    unique_symbols = "-@*=%/$#+&"
    in_file = "example.txt"
    visual = []
    part_locations=[]
    with open(in_file, "r") as infile:
        for line in infile:
            line = line.strip()
            visual.append([line])
    print(visual)
    for y in range(len(visual)-1):
        # print("y", y)
        # print(visual[y])
        for x in range(len(visual[y][0])-1):
            # print(visual[y][0][x])
            spot = visual[y][0][x]
            if spot.isdigit():
                continue
            elif spot in unique_symbols:
                part_locations.append((y,x))
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
    print(part_locations)
print(part1())