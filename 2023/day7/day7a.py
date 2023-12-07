hands = []
bids = []

with open('input.txt') as input:
    for line in input:
        hands.append(list(line.split()[0]))
        bids.append(line.split()[1])

# 5 of a kind: 6
# 4 of a kind: 5
# full house: 4
# 3 of a kind: 3
# two pair: 2
# one pair: 1
# high: 0

def hand_type(hand):
    card_freq = {}
    for card in hand:
        if card == card in card_freq:
            card_freq[card] += 1
        else:
            card_freq[card] = 1
    
    card_freq = dict(sorted(card_freq.items(), key=lambda item: item[1], reverse=True))
    if list(card_freq.values())[0] == 5:
        return 6
    if list(card_freq.values())[0] == 4:
        return 5
    if list(card_freq.values())[0] == 3:
        if list(card_freq.values())[1] == 2:
            return 4
        if list(card_freq.values())[1] == 1:
            return 3
    if list(card_freq.values())[0] == 2:
        if list(card_freq.values())[1] == 2:
            return 2
        if list(card_freq.values())[1] == 1:
            return 1
    return 0

def hand_as_num(hand):
    hand_num = []
    for card in hand:
        if card == "A":
            hand_num.append(14)
        elif card == "K":
            hand_num.append(13)
        elif card == "Q":
            hand_num.append(12)
        elif card == "J":
            hand_num.append(11)
        elif card == "T":
            hand_num.append(10)
        elif 10 > int(card) > 1:
            hand_num.append(int(card))
    return hand_num
        

new_hands = []
for i, hand in enumerate(hands):
    h2 = [hand_type(hand)] + hand_as_num(hand) + [int(bids[i])]
    new_hands.append(tuple(h2))

res = sorted(new_hands, key = lambda sub: (sub[0], sub[1], sub[2], sub[3], sub[4], sub[5] ))

total = 0
for i, h in enumerate(res):
    total += h[6]*(i+1)
