with open('input.txt') as f:
    lines = f.read().rstrip().split("\n")
bag_values = {
    'red': 12,
    'green': 13,
    'blue': 14
}
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

    flag = True
    for game_set in game_list:
        for k, v in game_set.items():
            if (v > bag_values[k]):
                flag = False
    if (flag is True):
        answer += game_id
print(f'Answer: {answer}')
