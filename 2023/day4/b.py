win_cards = []
my_cards = []

with open('input.txt') as input:
    for line in input:
        split_line = line.split("|")
        win_cards.append(split_line[0].split(":")[1].split())
        my_cards.append(split_line[1].split())


scorecards_won = [1] * len(win_cards)

for i in range(0,len(win_cards)): 
    card_matches = 0
    # Get the number of card matches for each line
    for j in range(0,len(win_cards[0])):
        for k in range(0,len(my_cards[0])):
            if (win_cards[i][j] == my_cards[i][k]): 
                card_matches += 1
                break
    # Add to scorecards_won
    if card_matches != 0:
        for n in range(1,card_matches+1):
            if i+n < len(scorecards_won):
                # Add the current number of scorecards to the next x scorecards (where x is "card_matches")
                scorecards_won[i+n] += scorecards_won[i]
    
print(sum(scorecards_won))