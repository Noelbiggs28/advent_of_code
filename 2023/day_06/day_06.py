# lasts blank miliseconds
# blank milimeterslong.
# can hold any number of whole miliseconds
# amount of time holding buttons is amount of milimeters per milisecond
# determine number different button hold times per race. and multiply them together
# example answer 288
def determine_ways_to_win(time, distance):
    time, distance= int(time), int(distance)
    first = None
    last = None
    # 7 miliseconds, 9 milimeters
    for second in range(1,time):
        if second * (time-second) > distance:
            first = second
            break
    for second in range(time-1, 0, -1):
        if second * (time-second) > distance:
            last = second
            break

    return last-first+1


def part1():
    in_file = "input.txt"
    ways_to_win = 1
    times=[]
    distances=[]
    with open(in_file, "r") as infile:
        for _ in infile:
            
            line = _.strip().split(":")
       
            if line[0] == "Time":
                numbers = line[1].split(' ')
                times = [number for number in numbers if number!=""]
            else:
                numbers = line[1].split(' ')
                distances = [number for number in numbers if number!=""]
    for race in range(len(times)):
        number_of_ways = determine_ways_to_win(times[race], distances[race])
        ways_to_win =ways_to_win * number_of_ways
    return ways_to_win
print(part1())
# its actually one big number
# answer71503
def part2():
    in_file = "input.txt"
    answer = None
    time = ''
    distance = ''
    with open(in_file, "r") as infile:
        for _ in infile:         
            line = _.strip().split(":")
            if line[0] == "Time":
                numbers = line[1].split(' ')
                for number in numbers:
                    if number != '':
                        time+=number
           
            else:
                numbers = line[1].split(' ')
                for number in numbers:
                    if number != '':
                        distance+=number
    answer = determine_ways_to_win(time,distance)
    return answer
print(part2())