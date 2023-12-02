with open('input.txt') as f:
    lines = f.read().rstrip().split("\n")
answer = 0
for line in lines:
    line = line.split(":")
    game_id = int(line[0].replace("Game ", ""))
    game = line[1]
    game_sets = game.split(";")
    game_list = []
    for set in game_sets:
        colors = set.split(",")
        color_dict = {}
        for color in colors:
            k = color.split()[1]
            v = color.split()[0]
            color_dict[k] = int(v)
        game_list.append(color_dict)

    lowest_bag = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    for game_set in game_list:
        for k, v in game_set.items():
            if (lowest_bag[k] < v):
                lowest_bag[k] = v
    power = lowest_bag["red"] * lowest_bag["green"] * lowest_bag["blue"]
    answer += power
print(f'Answer: {answer}')
