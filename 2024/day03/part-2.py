import re

with open("input.txt") as f:
    program = f.read().rstrip()


def mul(a, b):
    return a * b


enable = True
result = 0
matches = re.finditer(r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)", program)
for match in matches:
    if match.group() == "do()":
        enable = True
    elif match.group() == "don't()":
        enable = False
    elif enable:
        result += mul(*map(int, match.group().strip("mul()").split(",")))

print(result)
