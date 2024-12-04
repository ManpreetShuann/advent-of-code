with open("input.txt") as f:
    matrix = f.read().rstrip().splitlines()

count = 0
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if matrix[row][col] != "X":
            continue
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == 0 and j == 0:
                    continue
                if not (
                    0 <= row + 3 * i < len(matrix)
                    and 0 <= col + 3 * j < len(matrix[row])
                ):
                    continue
                if (
                    matrix[row + i][col + j] == "M"
                    and matrix[row + 2 * i][col + 2 * j] == "A"
                    and matrix[row + 3 * i][col + 3 * j] == "S"
                ):
                    count += 1
print(count)
