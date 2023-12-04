with open('input.txt') as f:
    input = f.read().rstrip().split("\n")

scratchcards = {}
for i, cards in enumerate(input):
    card = cards.split(": ")[1]
    win_num = card.split(" | ")[0].split()
    all_num = card.split(" | ")[1].split()
    count = 0
    for num in all_num:
        if num in win_num:
            count += 1

    if i not in scratchcards:
        scratchcards[i] = 1
    for j in range(i + 1, i + count + 1):
        scratchcards[j] = scratchcards.get(j, 1) + scratchcards[i]
total = sum(scratchcards.values())

print(f"Answer: {total}")
