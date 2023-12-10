from computer import Computer
from folder import Folder
from file import File


mac = Computer()
home_folder = mac.home
current_folder = home_folder
listing = False
with open('list_of_commands.txt', 'r') as infile:
    for line in infile:
        line = line.strip()
        row = line.split(' ')
        # print(f'current row {row}')
        # print(f'current folder {type(current_folder)}')
        # if command input given
        if listing == True:
            if row[0] == '$':
                listing = False
            elif row[0] == 'dir':
                # print(f'row[1] before  {row[1]}')
                row[1] = Folder(row[1], current_folder)
                # print(f'row[1] after  {row[1]}')
                current_folder.contents.append(row[1])
                mac.all_folder.append(row[1])
            else:
                row[1] = File(row[0], row[1])
                current_folder.contents.append(row[1])

        if row[0] == '$' and listing == False:
            # if cd
            if row[1] == 'cd':
                # go home
                if row[2] == '/':
                    current_folder = home_folder
                # go up one level
                elif row[2] == '..':
                    current_folder = current_folder.parent_folder
                #go to folder
                else: 
                    for folder in current_folder.contents:
                        if folder.name == row[2]:
                            current_folder = folder

            if row[1] == 'ls':
                listing = True
                

def find_size(folder):
    size = 0

    for thing in folder.contents:
        if isinstance(thing, File):
            size += thing.size
        elif isinstance(thing, Folder):
            size += find_size(thing)
    # print(size)
    # print(folder.name)
    return size

total_size = 0
for folder in mac.all_folder:
    size = find_size(folder) 
    if size <= 100000:
        total_size += size
# print(total_size)
deleted = 70000000
for folder in mac.all_folder:
    size = find_size(folder)
    if 8381165 < size < deleted:
        deleted = size
print(deleted)


