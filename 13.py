import re

with open("13.txt") as file:
    data = file.read()

pattern = re.compile("""Button A: X([\+\-]\d+), Y([\+\-]\d+)
Button B: X([\+\-]\d+), Y([\+\-]\d+)
Prize: X=(\-?\d+), Y=(\-?\d+)""")

corrected_number = 10000000000000


def calc_tokens(dx0, dy0, dx1, dy1, tx, ty):
    n = (dx0 * ty - dy0 * tx) / (dx1 * dy0 - dy1 * dx0)
    k = (tx + n * dx1) / dx0
    a_pressed = abs(k)
    b_pressed = abs(n)
    if a_pressed % 1 != 0 or b_pressed % 1 != 0:
        return 0
    return int(a_pressed * 3 + b_pressed)


tokens = 0
corrected_tokens = 0

for match in pattern.finditer(data):
    dx0, dy0, dx1, dy1, tx, ty = list(map(int, match.groups()))
    tokens += calc_tokens(dx0, dy0, dx1, dy1, tx, ty)
    tx += corrected_number
    ty += corrected_number
    corrected_tokens += calc_tokens(dx0, dy0, dx1, dy1, tx, ty)

print("Part 1:", tokens)
print("Part 2:", corrected_tokens)
