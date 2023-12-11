with open('input.txt') as f:
    input = f.read().rstrip().split("\n")


def extrapolate(row):
    if all(values == 0 for values in row):
        return 0
    differences = []
    for i in range(len(row) - 1):
        x = row
        y = row[1:]
        diff = y[i] - x[i]
        differences.append(diff)
    prediction = row[0] - extrapolate(differences)
    return prediction


total = 0
for rows in input:
    row = list(map(int, rows.split()))
    prediction = extrapolate(row)
    total += prediction
print(f"Answer: {total}")
