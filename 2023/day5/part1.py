with open('input.txt') as f:
    seeds = list(map(int, f.read().rstrip().split(
        "\n")[0].split(": ")[1].split()))
with open('input.txt') as f:
    maps = f.read().rstrip().split("\n\n")
input_maps = maps[1:]

mapping = []
for input_map in input_maps:
    input_map = input_map.split(" map:")
    map_key = input_map[0]
    map_values = input_map[1].split("\n")[1:]
    range_map = []
    for maps in map_values:
        range = list(map(int, maps.split()))
        range_map.append(range)
    seed_location = []
    for seed in seeds:
        for dr, sr, rl in range_map:
            if (sr + rl > seed >= sr):
                seed_location.append((seed - sr) + dr)
                break
        else:
            seed_location.append(seed)
    seeds = seed_location
Answer = min(seeds)

print(f"Answer: {Answer}")
