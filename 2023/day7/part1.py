"""
Every hand is exactly one type. From strongest to weakest, they are:

7 : Five of a kind, where all five cards have the same label: AAAAA
6 : Four of a kind, where four cards have the same label and one card has a different label: AA8AA
5 : Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
4 : Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
3 : Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
2 : One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
1 : High card, where all cards' labels are distinct: 23456

"""
with open('input.txt') as f:
    input = f.read().rstrip().split("\n")


def check_hand_type(hand):
    hand_strength = {
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6': 0,
        '7': 0,
        '8': 0,
        '9': 0,
        'T': 0,
        'J': 0,
        'Q': 0,
        'K': 0,
        'A': 0
    }
    for cards in hand:
        hand_strength[cards] += 1
    v = hand_strength.values()
    if (5 in v):
        return 7
    if (4 in v):
        return 6
    if (3 in v):
        if (2 in v):
            return 5
        return 4
    if (2 in v):
        if (list(v).count(2) > 1):
            return 3
        return 2
    return 1


def get_card_value(hand):
    hand = hand.replace('A', 'F')
    hand = hand.replace('K', 'E')
    hand = hand.replace('Q', 'D')
    hand = hand.replace('J', 'C')
    hand = hand.replace('T', 'B')
    return hand


h_b_t = []
for hands in input:
    hand = hands.split()[0]
    bid = hands.split()[1]
    hand_type = check_hand_type(hand)
    card_strength = get_card_value(hand)
    h_b_t.append({
        'hand': hand,
        'bid': int(bid),
        'type': hand_type,
        'card_strength': card_strength
    })

sorted_by_strength = sorted(
    h_b_t, key=lambda hbt: (hbt['type'], hbt['card_strength']))

tw = 0
for i, x in enumerate(sorted_by_strength):
    tw += (i + 1) * x['bid']
print(f"Answer: {tw}")
