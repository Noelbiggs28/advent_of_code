def count_data(file):
    file_tree = []
    how_deep = 0
    how_wide = 0
    with open(file, 'r') as infile:
        for line in infile:
            print(how_deep)
            line = line.strip()
            if line == '$ cd /':
                how_deep = 0
                continue
            elif line == "$ cd ..":
                how_deep -= 1
                continue
            elif line[0:4]=="$ cd":
                how_deep += 1
            elif line[0:3] == 'dir':
                if line[3:] not in file_tree:
                    file_tree[how_deep][how_wide] = line[3:]
                    how_wide += 1
            elif line == "$ ls":
                how_wide = 0
    return file_tree

print(count_data('practice.txt'))