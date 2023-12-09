def shoot():
    total_score = 0
    base_score = {
        'X':'1',
        'Y':'2',
        'Z':'3'
    }
    winning_score = {'A':{'X':'3','Y':'6','Z':'0'},
                     'B':{'X':'0','Y':'3','Z':'6'},
                     'C':{'X':'6','Y':'0','Z':'3'}}
    with open('strategy.txt', 'r') as infile:
        for line in infile:
            opponent = line[0].strip()
            me =line[2].strip()
            total_score += int(base_score[me]) 
            total_score += int(winning_score[opponent][me])
    return total_score 

def shoot2():
    total_score = 0
    winning_score = {
    'X':'0',
    'Y':'3',
    'Z':'6'
    }
    base_score = {'A':{'X':'3','Y':'1','Z':'2'},
                  'B':{'X':'1','Y':'2','Z':'3'},
                  'C':{'X':'2','Y':'3','Z':'1'}}
    with open('strategy.txt', 'r') as infile:
        for line in infile:
            opponent = line[0].strip()
            me =line[2].strip()
            total_score += int(winning_score[me]) 
            total_score += int(base_score[opponent][me])
    return total_score 
print(shoot())
print(shoot2())

def shoot3():
    score = {
            'A': 1,
            'B': 2,
            'C': 3,
            'X': 1,
            'Y': 2,
            'Z': 3,
        }
    player_02 = 0
    with open('strategy.txt', 'r') as infile:
        for line in infile:
            print(line[0], line[2])
            player_02 += score[line[2]]
            if score[line[0]] < score[line[2]]:
                player_02 += 6
            elif score[line[0]] == score[line[2]]:
                player_02 += 3
    return player_02
print(shoot3())