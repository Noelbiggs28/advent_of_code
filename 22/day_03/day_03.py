def find_priority():
    alpha = '3abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    total_priority = 0    
    with open('rucksack.txt', 'r') as infile:
        for line in infile:
            line = line.strip()
            length = int(len(line)/2)
            first = line[:length]
            last = line[length:]
            for letter in first:
                if letter in last:
                    total_priority += alpha.index(letter)
                    break
    return total_priority


def find_badge():
    alpha = '3abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    total_priority = 0    
    row = 0
    ls = ['a','b','c']
    with open('rucksack.txt', 'r') as infile:
        for line in infile:
            line = line.strip()
            ls[row]=line
            row += 1
            if row == 3:
                row = 0
                for letter in ls[0]:
                    if letter in ls[1] and letter in ls[2]:
                        total_priority += alpha.index(letter)
                        break
                        
    return total_priority

print(find_priority())
print(find_badge())