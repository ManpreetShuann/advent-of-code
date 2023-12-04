with open('input.txt') as f:
    input = f.read().rstrip().split("\n")

total = 0
for cards in input:
    card = cards.split(": ")[1]
    win_num = card.split(" | ")[0].split()
    all_num = card.split(" | ")[1].split()
    count = 0
    point = 0
    for num in all_num:
        if num in win_num:
            count += 1
    if count > 0:
        point = pow(2, count - 1)
    total += point

print(f"Answer: {total}")
