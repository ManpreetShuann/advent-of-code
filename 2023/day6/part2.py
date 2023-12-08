with open('input.txt') as f:
    input = f.read().rstrip().split("\n")

time = int("".join(input[0].split(":")[1].split()))
distance = int("".join(input[1].split(":")[1].split()))

ways = 0
for charging_time in range(0, time + 1):
    racetime = time - charging_time
    distance_travelled = racetime * charging_time
    if (distance_travelled > distance):
        ways += 1
Answer = ways
print(f"Answer: {Answer}")
