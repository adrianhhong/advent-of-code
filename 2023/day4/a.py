total = 0
win_cards = []
my_cards = []

with open('input.txt') as input:
    for line in input:
        split_line = line.split("|")
        win_cards.append(split_line[0].split(":")[1].split())
        my_cards.append(split_line[1].split())


for i in range(0,len(win_cards)): 
    card_matches = 0
    for j in range(0,len(win_cards[0])):
        for k in range(0,len(my_cards[0])):
            if (win_cards[i][j] == my_cards[i][k]): 
                card_matches += 1
                break
    if card_matches != 0:
        total += pow(2, card_matches-1)

print(total)