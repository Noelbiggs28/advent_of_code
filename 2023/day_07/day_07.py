# example answer 6440
#five of a kind, = 7
# four of a kind, = 6 
# full house, = 5
# three of kind, = 4 
# two pair, = 3
# one pair,  = 2
# high card = 1

# determine what each hand is
# if tie goes by first card then second
# rank them with 1 being the lowest.
# multiply rank by bet. add all results


def determine_hand(hand, bet):
    three = None
    two = None
    
    number_of_pairs = 0
    cards = [card for card in hand]
    converter = {
        "T" : 10,
        "J" : 11,
        "Q" : 12,
        "K" : 13,
        "A" : 14
    }
    number_of_each_card = {}
    for i, card in enumerate(cards):
        if card in converter:
            cards[i] = converter[card]
        else:
            cards[i] = int(cards[i])
        if cards[i] in number_of_each_card:
            number_of_each_card[cards[i]] += 1
        else:
            number_of_each_card[cards[i]] = 1 
    # determine 5 of a kind
    if 5 in number_of_each_card.values():
        return ("five_of_a_kind", int(bet),cards)
    # determine 4 of a kind
    elif 4 in number_of_each_card.values():
        return ("four_of_a_kind", int(bet),cards)
    # determine full house/ 3 of a kind
    if 3 in number_of_each_card.values():
        for key in number_of_each_card.values():
            if key == 3:
                three = True
            if key == 2:
                two = True
        if three and two:
            return ("full_house", int(bet), cards)
        else:
            return ("three_of_a_kind", int(bet), cards)
    # determine 2 pair, 1 pair
    if 2 in number_of_each_card.values():
        for key in number_of_each_card.values():
            if key == 2:
                number_of_pairs += 1
        if number_of_pairs == 2:
            return ("two_pair", int(bet), cards)
        else:
            return ("one_pair", int(bet), cards)
    return ("high_card", int(bet), cards)
        



def part1():
    total_winnings = 0
    current_ranking = 1
    in_file = "input.txt"
    hands_and_bets = []
    all_hand_strenghts = {
        "high_card": [],
        "one_pair" : [],
        "two_pair" : [],
        "three_of_a_kind" : [],
        "full_house" : [],
        "four_of_a_kind":[],
        "five_of_a_kind":[]
        }
    with open(in_file, "r") as infile:
        for _ in infile:
            line = _.strip().split(' ')
            hands_and_bets.append([line[0],line[1]])
    for player in hands_and_bets:
        hand_strength = determine_hand(player[0], player[1])
        all_hand_strenghts[hand_strength[0]].append(hand_strength[1:])
    for hand_type in all_hand_strenghts.keys():
        if len(all_hand_strenghts[hand_type]) == 1:
            total_winnings += all_hand_strenghts[hand_type][0][0] * current_ranking
            current_ranking+=1
            continue
        if len(all_hand_strenghts[hand_type]) >1:

            all_hand_strenghts[hand_type] = sorted(all_hand_strenghts[hand_type], key=lambda x: x[1])
            for hand in all_hand_strenghts[hand_type]:

                total_winnings += hand[0] * current_ranking
                current_ranking += 1
                
 

    return total_winnings
print(part1())
# example answer 6440