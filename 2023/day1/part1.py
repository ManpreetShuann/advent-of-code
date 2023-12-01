with open('input.txt') as f:
    lines = f.read()
num_list = []

for line in lines.split("\n"):
    number = ""
    for letter in line:
        if (letter.isdigit()):
            number = number + letter
    number = number[0] + number[-1]
    number = int(number)
    num_list.append(number)

total = 0
for number in num_list:
    total = total + number

print(f"Answer= {total}")
