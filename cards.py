import itertools
import random

card_deck1 = list(itertools.product(["A", '2', '3', '4', '5', '6', '7', '8', '9', '10', "Jack", "Queen", "King"],
                                    ["Spade", "Club", "Diamond", "Heart"]))
card_deck2 = list(itertools.product(["A", '2', '3', '4', '5', '6', '7', '8', '9', '10', "Jack", "Queen", "King"],
                                    ["Spade", "Club", "Diamond", "Heart"]))
random.shuffle(card_deck1)
random.shuffle(card_deck2)

for i in range(1, 52):
    if card_deck1[i][0] == card_deck2[i][0]:
        print("SNAP")
        print(card_deck1[i][0] + card_deck1[i][1], card_deck2[i][0] + card_deck2[i][1])
    pass