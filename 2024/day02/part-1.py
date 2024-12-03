with open("input.txt") as f:
    reports = f.read().rstrip().split("\n")
count = 0
for report in reports:
    report = report.split()
    report = list(map(int, report))
    flag = "unsafe"
    if report == sorted(report) or report == sorted(report, reverse=True):
        for i in range(0, len(report) - 1):
            if 1 <= (abs(report[i] - report[i + 1])) <= 3:
                flag = "safe"
            else:
                flag = "unsafe"
                break
    if flag == "safe":
        count += 1

print(count)
