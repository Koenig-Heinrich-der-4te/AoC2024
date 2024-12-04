with open("04.txt") as file:
    data = file.read()

matrix = data.splitlines()


def getchar(x, y):
    if 0 <= x < len(matrix) and 0 <= y < len(matrix[x]):
        return matrix[x][y]
    return ""


x_mas = ["M.S", ".A.", "M.S"]
rotations = []
for i in range(4):
    rotations.append(x_mas)
    x_mas = [
        [x_mas[j][i] for j in range(len(x_mas))]
        for i in range(len(x_mas[0]) - 1, -1, -1)
    ]


def check_pattern(x, y, rotation):
    rotation = rotations[rotation]

    for dx in range(3):
        for dy in range(3):
            required_char = rotation[dx][dy]
            if required_char != "." and getchar(x + dx, y + dy) != required_char:
                return False

    return True


maximum = max(len(matrix), len(matrix[0]))
count = 0

for x in range(maximum):
    for y in range(maximum):
        for rotation in range(4):
            if check_pattern(x, y, rotation):
                count += 1

print("Part 2:", count)
