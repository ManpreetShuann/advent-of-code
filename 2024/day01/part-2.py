with open("input.txt") as f:
    lines = f.read().split("\n")
lines.pop()
first_list = []
second_list = []

for line in lines:
    first_list.append(line.split()[0])
    second_list.append(line.split()[1])
first_list.sort()
second_list.sort()

similarity_score_list = []

for number in first_list:
    number = int(number)
    count = 0
    for i in range(len(second_list)):
        if number == int(second_list[i]):
            count += 1
    similarity_score = number * count
    similarity_score_list.append(similarity_score)

print(sum(similarity_score_list))
