def shoot():
    total_score = 0
    # base_score = {
    #     'X':'1',
    #     'Y':'2',
    #     'Z':'3'
    # }
    base_score = {
        'X':'0',
        'Y':'3',
        'Z':'6'
    }
    # winning_score = {'A':{'X':'3','Y':'6','Z':'0'},'B':{'X':'0','Y':'3','Z':'6'},'C':{'X':'6','Y':'0','Z':'3'}}
    winning_score = {'A':{'X':'3','Y':'1','Z':'2'},'B':{'X':'1','Y':'2','Z':'3'},'C':{'X':'2','Y':'3','Z':'1'}}
    with open('strategy.txt', 'r') as infile:
        for line in infile:
            opponent = line[0].strip()
            me =line[2].strip()
            total_score += int(base_score[me]) 
            total_score += int(winning_score[opponent][me])
    return total_score 
print(shoot())