with open("input.txt") as f:
    sections = f.read().rstrip().split("\n\n")

ordering = sections[0].split("\n")
ordering = [orders.split("|") for orders in ordering]
updates = sections[1].split("\n")
updates = [update.split(",") for update in updates]

rules = {}
for i, j in ordering:
    rules[i, j] = True
    rules[j, i] = False


def check_if_ordered(update):
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            if (update[i], update[j]) in rules and rules[update[i], update[j]] is False:
                return False
    return True


total = 0
for update in updates:
    if check_if_ordered(update):
        total += int(update[len(update) // 2])

print(total)
