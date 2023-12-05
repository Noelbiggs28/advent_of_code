# example answer is 13
# get a scratch card card 1: winning numbers | your numbers
# first match is one point double every next one
def part1():
    in_file = "input.txt"
    total_points = 0
    with open(in_file, "r") as infile:
        for _ in infile:
            line = _.strip()
            # separate useful infro from card number
            numbers = line.split(':')[1]
            # get a list of winning numbers
            winning_numbers = numbers.split("|")[0].strip().split(' ')
            # get a list of your number and remove blanks spaces
            your_numbers = numbers.split("|")[1].strip().split(' ')
            your_numbers = [number for number in your_numbers if len(number) > 0]
            # create a dictionary of winning numbers
            winning_numbers_dict = {"points":0}
            for winning_number in winning_numbers:
                winning_numbers_dict[winning_number] = True
            # check if your number is in the dictionary and apply math
            for your_number in your_numbers:
                try:
                    if winning_numbers_dict[your_number]:
                        if winning_numbers_dict['points'] == 0:
                            winning_numbers_dict['points'] = 1
                        else: 
                            winning_numbers_dict['points'] = winning_numbers_dict['points'] * 2
                except KeyError: 
                    continue
            total_points += winning_numbers_dict['points']         
    return total_points
print(part1())
# 115037 too high

# example answer is 30
# get a scratch card card 1: winning numbers | your numbers
# the number of matchs on the card you get a copy of the next that many cards.
# copys also win copies. how many cards do you end up with
def part2():
    in_file = "example.txt"
    total_points = 0
    with open(in_file, "r") as infile:
        for _ in infile:
            line = _.strip()
            # separate useful infro from card number
            numbers = line.split(':')[1]
            # get a list of winning numbers
            winning_numbers = numbers.split("|")[0].strip().split(' ')
            # get a list of your number and remove blanks spaces
            your_numbers = numbers.split("|")[1].strip().split(' ')
            your_numbers = [number for number in your_numbers if len(number) > 0]
            # create a dictionary of winning numbers
            winning_numbers_dict = {"points":0}
            for winning_number in winning_numbers:
                winning_numbers_dict[winning_number] = True
            # check if your number is in the dictionary and apply math
            for your_number in your_numbers:
                try:
                    if winning_numbers_dict[your_number]:
                        if winning_numbers_dict['points'] == 0:
                            winning_numbers_dict['points'] = 1
                        else: 
                            winning_numbers_dict['points'] = winning_numbers_dict['points'] * 2
                except KeyError: 
                    continue
            total_points += winning_numbers_dict['points']         
    return total_points
print(part2())