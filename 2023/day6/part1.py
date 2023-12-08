with open('input.txt') as f:
    input = f.read().rstrip().split("\n")

times = list(map(int, input[0].split(":")[1].split()))
distances = list(map(int, input[1].split(":")[1].split()))

Answer = 1
for i, time in enumerate(times):
    ways = 0
    for charging_time in range(0, time + 1):
        racetime = time - charging_time
        distance_travelled = racetime * charging_time
        if (distance_travelled > distances[i]):
            ways += 1
    Answer *= ways
print(f"Answer: {Answer}")
