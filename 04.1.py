with open("04.txt") as file:
    data = file.read()

matrix = data.splitlines()


def getchar(x, y):
    if 0 <= x < len(matrix) and 0 <= y < len(matrix[x]):
        return matrix[x][y]
    return ""


def check_direction(x, y, dx, dy):
    for i in range(4):
        rx, ry = x - i * dx, y - i * dy
        if getchar(rx, ry) != xmas[i]:
            return False
    return True


maximum = max(len(matrix), len(matrix[0]))
xmas = "XMAS"
count = 0

for x in range(maximum):
    for y in range(maximum):
        if getchar(x, y) != xmas[0]:
            continue
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue
                if check_direction(x, y, dx, dy):
                    count += 1

print("Part 1:", count)
