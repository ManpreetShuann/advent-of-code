with open('input.txt') as f:
    input = f.read().rstrip().split("\n\n")

instructions = input[0]
nodes = input[1].split("\n")

directions = {}
for node in nodes:
    k, v = node.split(" = ")
    v1, v2 = v.replace("(", "").replace(")", "").split(", ")
    v = (v1, v2)
    directions[k] = v

steps = 0
navigate = "AAA"
while True:
    for instruction in instructions:
        if instruction == 'L':
            navigate = directions[navigate][0]
        else:
            navigate = directions[navigate][1]
        steps += 1
    if navigate == "ZZZ":
        break

print(f"Answer: {steps}")
