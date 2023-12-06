# convert until location found for each seed. find lowest location
def part1():
    in_file = "example.txt"
    info = {}
    converter = ''
    with open(in_file, 'r') as infile:
        for _ in infile:
            line = _.strip()
            if line == '':
                continue
      
            if line[:5] == "seeds":
                line = line.split(':')
                info[line[0]] = line[1].strip().split(' ')
                continue
            elif line[-1] ==":":
                converter = line.split(" ")[0]
                info[converter] = []
            info[converter].append(line.split(" "))
    print(info)
print(part1())