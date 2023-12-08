with open('input.txt') as f:
    input_seeds = list(map(int, f.read().rstrip().split(
        "\n")[0].split(": ")[1].split()))
with open('input.txt') as f:
    maps = f.read().rstrip().split("\n\n")
input_maps = maps[1:]

seeds = []
mapping = []
for i in range(0, len(input_seeds), 2):
    seeds.append((input_seeds[i], input_seeds[i] + input_seeds[i + 1]))

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
        start = seed[0]
        end = seed[1]
        for dr, sr, rl in range_map:
            overlap_start = max(sr, start)
            overlap_end = min(end, sr + rl)
            if (overlap_start < overlap_end):
                seed_location.append((
                    overlap_start - sr + dr, overlap_end - sr + dr))
                if (overlap_start > start):
                    seeds.append((start, overlap_start))
                if (end > overlap_end):
                    seeds.append((overlap_end, end))
                break
        else:
            seed_location.append((start, end))
    seeds = seed_location
Answer = min(seeds)[0]

print(f"Answer: {Answer}")
