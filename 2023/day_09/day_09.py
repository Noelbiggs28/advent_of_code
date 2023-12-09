def find_next_number(data_set):
    next_data_set =[]
    x=0
    for index in range(len(data_set)-1):
        x = data_set[index+1] - data_set[index]
        next_data_set.append(x)

    if all([number==0 for number in next_data_set]):
        return data_set[-1]
    else:
        return data_set[-1] + find_next_number(next_data_set) 


def part1():
    answer = 0
    in_file = "input.txt"
    info = []
    with open(in_file, "r") as infile:
        for _ in infile:
            line = _.strip().split(' ')
            line = [int(number) for number in line]
            info.append(line)
    for data_set in info:
        next_number = find_next_number(data_set)
        answer += next_number

    return answer
print(part1())

def find_prev_number(data_set):
    next_data_set =[]
    x=0
    for index in range(len(data_set)-1):
        x = data_set[index] - data_set[index+1]
        next_data_set.append(x)


    if all([number==0 for number in next_data_set]):
        return data_set[-1]
    else:
        return data_set[-1] - find_prev_number(next_data_set) 

def part2():
    answer = 0
    in_file = "input.txt"
    info = []
    with open(in_file, "r") as infile:
        for _ in infile:
            line = _.strip().split(' ')[::-1]
            line = [int(number) for number in line]

            info.append(line)
    for data_set in info:
        next_number = find_prev_number(data_set)
        answer += next_number

    return answer
print(part2())