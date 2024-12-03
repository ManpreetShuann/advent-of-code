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

distance_list = []
for i in range(len(first_list)):
    distance_list.append(abs(int(first_list[i]) - int(second_list[i])))

print(sum(distance_list))
