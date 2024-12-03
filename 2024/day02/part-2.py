with open("input.txt") as f:
    reports = f.read().rstrip().split("\n")
count = 0


def is_safe(report):
    diffs = [(report[i] - report[i + 1]) for i in range(0, len(report) - 1)]
    return all([1 <= diff <= 3 for diff in diffs]) or all(
        [-3 <= diff <= -1 for diff in diffs]
    )


for report in reports:
    report = report.split()
    report = list(map(int, report))
    if any(is_safe(report[:i] + report[i + 1 :]) for i in range(len(report))):
        count += 1
print(count)
