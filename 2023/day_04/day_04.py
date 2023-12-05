# example answer is 13
# get a scratch card card 1: winning numbers | your numbers
# first match is one point double every next one
def part1():
    in_file = "example.txt"
    total_points = 0
    with open(in_file, "r") as infile:
        for _ in infile:
            line = _.strip()
            numbers = line.split(':')[1]
            winning_numbers = numbers.split("|")[0].strip().split(' ')
            your_numbers = numbers.split("|")[1].strip().split(' ')
            winning_numbers_dict = {"points":0}
            for winning_number in winning_numbers:
                winning_numbers_dict[winning_number] = True
            for your_number in your_numbers:
                if winning_numbers_dict[your_number]:
                    if winning_numbers_dict['points'] == 0:
                        winning_numbers_dict = 1
                    else: 
                        winning_numbers_dict['points'] = winning_numbers_dict['points'] * 2
            total_points += winning_numbers_dict['points']
    return total_points
print(part1())