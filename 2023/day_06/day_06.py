def part1():
    in_file = "example.txt"
    info = {}
    with open(in_file, "r") as infile:
        for _ in infile:
            line = _.strip().split(":")
            numbers = line[1].split(' ')
            numbers = [number for number in numbers if number!=""]
            info[line[0]] = numbers
            print(numbers)
            print(info)
print(part1())