with open('input.txt') as f:
    matrix = f.read().rstrip().split("\n")


def find_adjacent_cords(x, y, row_len, col_len):
    adjacent_cords = [
        (x - 1, y - 1),
        (x - 1, y),
        (x - 1, y + 1),
        (x, y - 1),
        (x, y + 1),
        (x + 1, y - 1),
        (x + 1, y),
        (x + 1, y + 1),
    ]
    valid_cords = []
    for i, j in adjacent_cords:
        if (col_len > i >= 0 and j > row_len >= 0):
            valid_cords.append((i, j))
    return adjacent_cords


col_len = len(matrix[0])
row_len = len(matrix)


symbol_list = []
for x, row in enumerate(matrix):
    for y, col in enumerate(row):
        if not col.isdigit() and not col == '.':
            symbol_list.append((x, y))


adjacent_cords = []
for x, y in symbol_list:
    adjacent_cords.extend(find_adjacent_cords(x, y, row_len, col_len))


part_numbers = []
counted_cords = []
for x, y in adjacent_cords:
    if (x, y) not in counted_cords:
        if matrix[x][y].isdigit():
            counted_cords.append((x, y))
            if matrix[x][y - 1].isdigit():
                counted_cords.append((x, y - 1))
                if matrix[x][y - 2].isdigit():
                    part_numbers.append(int(matrix[x][y - 2: y + 1]))
                    counted_cords.append((x, y - 2))
                else:
                    if matrix[x][y + 1].isdigit():
                        part_numbers.append(int(matrix[x][y - 1: y + 2]))
                        counted_cords.append((x, y + 1))
                    else:
                        part_numbers.append(int(matrix[x][y - 1: y + 1]))
            else:
                if matrix[x][y + 1].isdigit():
                    counted_cords.append((x, y + 1))
                    if matrix[x][y + 2].isdigit():
                        part_numbers.append(int(matrix[x][y: y + 3]))
                        counted_cords.append((x, y + 2))
                    else:
                        part_numbers.append(int(matrix[x][y: y + 2]))
                else:
                    part_numbers.append(int(matrix[x][y: y + 1]))

ANSWER = sum(part_numbers)
print(f"Answer: {ANSWER}")
