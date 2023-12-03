import re
with open('input.txt') as f:
    matrix = f.read().rstrip().split("\n")


# def find_adjacent_cords(x, y, row_len, col_len):
#     adjacent_cords = [
#         (x - 1, y - 1),
#         (x - 1, y),
#         (x - 1, y + 1),
#         (x, y - 1),
#         (x, y + 1),
#         (x + 1, y - 1),
#         (x + 1, y),
#         (x + 1, y + 1),
#     ]
#     valid_cords = []
#     for i, j in adjacent_cords:
#         if (col_len > i >= 0 and j > row_len >= 0):
#             valid_cords.append((i, j))
#     return adjacent_cords


# col_len = len(matrix[0])
# row_len = len(matrix)


# gear_list = []
# for x, row in enumerate(matrix):
#     for y, col in enumerate(row):
#         if col == '*':
#             gear_list.append((x, y))

# ANSWER = 0
# for i, j in gear_list:
#     gear_adjacent_numbers = []
#     adjacent_cords = find_adjacent_cords(i, j, row_len, col_len)
#     for x, y in adjacent_cords:
#         if matrix[x][y].isdigit():
#             if matrix[x][y - 1].isdigit():
#                 if matrix[x][y - 2].isdigit():
#                     gear_adjacent_numbers.append(int(matrix[x][y - 2: y + 1]))
#                 else:
#                     if matrix[x][y + 1].isdigit():
#                         gear_adjacent_numbers.append(
#                             int(matrix[x][y - 1: y + 2]))
#                     else:
#                         gear_adjacent_numbers.append(
#                             int(matrix[x][y - 1: y + 1]))
#             else:
#                 if matrix[x][y + 1].isdigit():
#                     if matrix[x][y + 2].isdigit():
#                         gear_adjacent_numbers.append(int(matrix[x][y: y + 3]))
#                     else:
#                         gear_adjacent_numbers.append(int(matrix[x][y: y + 2]))
#                 else:
#                     gear_adjacent_numbers.append(int(matrix[x][y: y + 1]))
#     gears = list(set(gear_adjacent_numbers))
#     if len(gears) == 2:
#         ANSWER += gears[0] * gears[1]
# print(f"Answer: {ANSWER}")


number_cords = []
symbol_cords = []
for x, row in enumerate(matrix):
    numbers = re.finditer(r'\d+', row)
    for num in numbers:
        cords = []
        for i in range(len(num.group())):
            cords.append((x, num.start() + i))
        number_cords.append([int(num.group()), cords])
    symbols = re.finditer(r'[*]', row)
    for sym in symbols:
        symbol_cords.append([sym.group(), (x, sym.start()), []])
for num in number_cords:
    for cord in num[1]:
        for sym in symbol_cords:
            if abs(cord[0] - sym[1][0]) <= 1 and abs(cord[1] - sym[1][1]) <= 1:
                if num not in sym[2]:
                    sym[2].append(num)
                break
gear_ratios = []

for sym in symbol_cords:
    if len(sym[2]) == 2:
        gear_ratios.append(sym[2][0][0] * sym[2][1][0])
ANSWER = sum(gear_ratios)
print(f"Answer: {ANSWER}")
