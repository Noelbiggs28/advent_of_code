# find the first and last digit in each line
def part1(in_file):  
 
    grand_total = 0
    with open(in_file, 'r') as infile:
        for _ in infile:
            line = _.strip()
            # remove nonnumbers
            numbers = ''.join(filter(lambda x: x.isdigit(), line))
            # combine first and last number as string
            total = numbers[0] + numbers[-1]
            # add it to total
            grand_total += int(total)
    return grand_total

print(part1("example.txt"))
# find the first and last digit in each line but digits can be spelled out
def part2(in_file):
    def find_all_indexs(word, string):
        temp = (string.find(word),word)
        if temp[0] == -1:
            return []
        return [temp] + (find_all_indexs(word, string[temp[0]+1:]))
    conversion = {
        "one":"1",
        "two":"2",
        "three":"3",
        "four":"4",
        "five":"5",
        "six":"6",
        "seven":"7",
        "eight":"8",
        "nine":"9"
    
    }
   
    grand_total = 0
    with open(in_file, 'r') as infile:
        for _ in infile:
            all_indexs_of_words = []
            line = _.strip().lower()

            for word in conversion:
                all_indexs_of_words.append(find_all_indexs(word, line))

            all_indexs_of_words = sorted([tupple for tupple in all_indexs_of_words if tupple!=[]])

            # print(first_and_last)
            # print(all_indexs_of_words)
            for index in range(len(all_indexs_of_words)):
                current_word = all_indexs_of_words[index][0][1]
                current_index = all_indexs_of_words[index][0][0]
                
                if index == 0 or index ==len(all_indexs_of_words) -1:
                    line = line.replace(current_word,conversion[current_word])
        
            numbers = ''.join(filter(lambda x: x.isdigit(), line))
            # combine first and last number as string
         
            total = numbers[0] + numbers[-1]
            # add it to total
            grand_total += int(total)
    return grand_total
# 53902 too high
# 53926 too high
print(part2("example3.txt"))
# eightwothree needs to be 83 not 23


