def part1(instructions):
    ls=['zero',
     'FCPGQR'
    , 'WTCP'
    , 'BHPMC'
    , 'LTQSMPR'
    , 'PHJZVGN'
    , 'DPJ'
    , 'LGPZFJTR'
    , 'NLHCFPTJ'
    , 'GVZQHTCW'
    ]
    with open(instructions, 'r')  as infile:
        for line in infile:
            line = line.strip()
            arr = line.split(' ')
            move = int(arr[1])
            begin = int(arr[3])
            to = int(arr[5])
            crate= ls[begin][-move:]
            crate = crate[::-1]
            ls[begin] = ls[begin][:-move]
            ls[to] = ls[to] + crate
    return ls
# WJVRLSJJT
# DHBJQJCCW
#
print(part1('instructions.txt'))
# blocks are moved one at a time