with open("02.txt") as file:
    data = file.read()


def sign(n):
    if n == 0:
        return 0
    return n // abs(n)


def check_report(report):
    first, second, *_ = report
    if first == second:
        return False
    growth_direction = sign(first - second)

    for a, b in zip(report, report[1:]):
        if not (1 <= abs(a - b) <= 3 and sign(a - b) == growth_direction):
            return False

    return True


safe_reports = 0
dampened_safe_reports = 0


for row in data.splitlines():
    report = [int(n) for n in row.split()]
    if check_report(report):
        safe_reports += 1
        dampened_safe_reports += 1
    else:
        for i in range(len(report)):
            short_report = report[:]
            del short_report[i]
            if check_report(short_report):
                dampened_safe_reports += 1
                break


print("Part 1:", safe_reports)
print("Part 2:", dampened_safe_reports)
