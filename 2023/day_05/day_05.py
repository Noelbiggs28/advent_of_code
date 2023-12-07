# convert until location found for each seed. find lowest location
def check_if_between(seed, output, input, range):
    seed, output, input, range = int(seed), int(output), int(input), int(range)
    print(seed, output, input, range)
    print(input, "<=", seed, "<", input+range)
    if input <= seed < input + range:
        return output + seed - input
    return -1


def part1():
    closest_seed = []
    in_file = "input.txt"
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
                continue
            info[converter].append(line.split(" "))
    for seed in info['seeds']:
        inner = seed
        for conversion_name in info.keys():
            print(conversion_name)
            if conversion_name == "seeds":
                continue
            for conversion in info[conversion_name]:
                next_seed = check_if_between(inner, conversion[0], conversion[1], conversion[2])
                if next_seed == -1:
                    continue
                else:
                    inner = next_seed
                    print(conversion_name, inner)
                    break
        closest_seed.append(inner)
            

            
    print(closest_seed)
    return min(closest_seed)
print(part1())