with open("input.txt") as f:
    matrix = f.read().rstrip().splitlines()

count = 0
for row in range(1, len(matrix) - 1):
    for col in range(1, len(matrix[row]) - 1):
        if matrix[row][col] != "A":
            continue
        corners = [
            matrix[row - 1][col - 1],
            matrix[row - 1][col + 1],
            matrix[row + 1][col + 1],
            matrix[row + 1][col - 1],
        ]
        corners = "".join(corners)
        if corners in ["MMSS", "SSMM", "SMMS", "MSSM"]:
            count += 1
print(count)
