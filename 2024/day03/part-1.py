import re

with open("input.txt") as f:
    program = f.read().rstrip()


def mul(a, b):
    return a * b


result = 0
matches = re.finditer(r"mul\(\d{1,3},\d{1,3}\)", program)
for match in matches:
    result += mul(*map(int, match.group().strip("mul()").split(",")))

print(result)
