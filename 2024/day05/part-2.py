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


def order_updates(updates):
    for i in range(len(updates)):
        for j in range(i + 1, len(updates)):
            if (updates[i], updates[j]) in rules and rules[
                updates[i], updates[j]
            ] is False:
                updates[i], updates[j] = updates[j], updates[i]
    return updates


total = 0
incorrectly_ordered = []
for update in updates:
    if not check_if_ordered(update):
        incorrectly_ordered.append(order_updates(update))

for update in incorrectly_ordered:
    total += int(update[len(update) // 2])

print(total)
