# fine the first and last digit in each line
def part1():  
    in_file = "input.txt"  
    grand_total = 0
    with open(in_file, 'r') as infile:
        for _ in infile:
            line = _.strip()
            # remove nonnumbers
            numbers = ''.join(filter(lambda x: x.isdigit(), line))
            # combine first and last number as string
            total = numbers[0] + numbers[-1]
            # print("line",line)
            # print("numbers", numbers)
            # print("total", total)
            # add it to total
            grand_total += int(total)
    return grand_total


# find the first and last digit in each line but digits can be spelled out
def part2():
    conversion = {
        "one":"1",
        "two":"2",
        "three":"3",
        "four":"4",
        "five":"5",
        "six":"6",
        "seven":"7",
        "eight":"8",
        "nine":"9",
        "zero":"0"
    }
    in_file = "example2.txt"  
    grand_total = 0
    with open(in_file, 'r') as infile:
        for _ in infile:
            line = _.strip().lower()
            for word in conversion:
                if word in line:
                    # replace written words with digits
                    line = line.replace(word,conversion[word])
            # numbers = ''.join(filter(lambda x: x.isdigit(), line))
            
            # total = numbers[0] + numbers[-1]
            print("line",line)
            # print("numbers", numbers)
            # print("total", total)
            # grand_total += int(total)
    return grand_total
print(part2())
# eightwothree needs to be 83 not 23