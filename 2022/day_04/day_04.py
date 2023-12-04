def contained(file):
    total_all_included = 0
    with open(file, 'r') as infile:
        for line in infile:
            line = line.strip()
            arr = line.split(',')
            arr2 = arr[0].split('-')
            arr3 = arr[1].split('-')
            if int(arr3[0])<=int(arr2[0])<=int(arr3[1]) and int(arr3[0])<=int(arr2[1])<=int(arr3[1]) or int(arr2[0])<=int(arr3[0])<=int(arr2[1]) and int(arr2[0])<=int(arr3[1])<=int(arr2[1]):
                total_all_included += 1

    return total_all_included

print(contained('cleaning.txt'))

# #193 is too low
# #added = signs
# #472 too low
# added ints to line 9

def overlap(file):
    total_overlapped = 0
    with open(file, 'r') as infile:
        for line in infile:
            line = line.strip()
            arr = line.split(',')
            arr2 = arr[0].split('-')
            arr3 = arr[1].split('-')
            arr4 = [num for num in range(int(arr2[0]), int(arr2[1])+1)]
            arr5 = [num for num in range(int(arr3[0]), int(arr3[1])+1)]
            arr6 = arr4+arr5
            before = len(arr6)
            after = len(set(arr6))
            diff = before - after
            if diff > 0:
                total_overlapped += 1
            # total_overlapped += diff
    return total_overlapped

print(overlap('cleaning.txt'))

#23185 is too high
#I counted how many sections overlapped vice how many pairs