with open('input.txt') as f:
    lines = f.read()
num_list = []
word_to_digit = {
    'one': 'o1e',
    'two': 't2o',
    'three': 'th3ee',
    'four': 'fo4r',
    'five': 'fi5e',
    'six': 's6x',
    'seven': 'se7en',
    'eight': 'ei8ht',
    'nine': 'ni9e'
}


def convert_to_number(word):
    for k, v in word_to_digit.items():
        if (k in word):
            word = word.replace(k, v)
    return word


for line in lines.split("\n"):
    line = convert_to_number(line)
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
