import math
with open('input.txt') as f:
    input = f.read().rstrip().split("\n\n")

instructions = input[0]
nodes = input[1].split("\n")


def ArrayLCM(array):
    lcm = array[0]
    for i in range(1, len(array)):
        lcm = lcm * array[i] // math.gcd(lcm, array[i])
    return lcm


directions = {}
for node in nodes:
    k, v = node.split(" = ")
    v1, v2 = v.replace("(", "").replace(")", "").split(", ")
    v = (v1, v2)
    directions[k] = v
useful_keys = [k for k in directions if k.endswith("A")]

cycles = []

for navigate in useful_keys:
    cycle = []
    current_instructions = instructions
    steps = 0
    first_occurence_z = None

    while True:
        while steps == 0 or not navigate.endswith("Z"):
            steps += 1
            if current_instructions[0] == 'L':
                navigate = directions[navigate][0]
            else:
                navigate = directions[navigate][1]
            current_instructions = current_instructions[1:] + \
                current_instructions[0]
        if first_occurence_z is None:
            # this is the first occurence
            first_occurence_z = navigate
            cycle.append(steps)
            steps = 0
        elif navigate == first_occurence_z:
            # cycle back at first occurence
            cycle.append(steps)
            break
        else:
            cycle.append(steps)
    cycles.append(cycle)

steps = [x[0] for x in cycles]
ANSWER = ArrayLCM(steps)

print(f"Answer: {ANSWER}")
