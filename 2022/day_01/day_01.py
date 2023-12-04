def find_highest():    
    elfs_load = 0
    elves = []
    with open('elves.txt', 'r') as infile:
        for line in infile:
            if len(line.strip()) > 0:
                elfs_load += int(line.strip())
            else:
                elves.append(elfs_load)
                elfs_load = 0
        elves.append(elfs_load)
    top1 = max(elves)
    asc_elves = sorted(elves)
    top3 = sum(asc_elves[-3:])
    print(top1)
    return top3
print(find_highest())
