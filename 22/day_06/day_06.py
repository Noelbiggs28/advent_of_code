def start(file):
    string = ''
    with open(file, 'r') as infile:
        for line in infile:
            string = line.strip()
    pointer_1 = 0
    pointer_2 = 4
    while pointer_2 < len(string):
        if len(string[pointer_1:pointer_2]) == len(set(string[pointer_1:pointer_2])):
            return pointer_2
        else:
            pointer_1 += 1
            pointer_2 += 1

def start_message(file):
    string = ''
    with open(file, 'r') as infile:
        for line in infile:
            string = line.strip()
    pointer_1 = 0
    pointer_2 = 14
    while pointer_2 < len(string):
        if len(string[pointer_1:pointer_2]) == len(set(string[pointer_1:pointer_2])):
            return pointer_2
        else:
            pointer_1 += 1
            pointer_2 += 1
print(start('practice.txt'))
print(start_message('practice.txt'))