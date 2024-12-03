import re

with open("03.txt") as file:
    data = file.read()

mul_sum = 0
accurate_mul_sum = 0
mul_enabled = True

for m in re.finditer("mul\(([0-9]+),([0-9]+)\)|do\(\)|don't\(\)", data):
    if m.group() == "do()":
        mul_enabled = True
    elif m.group() == "don't()":
        mul_enabled = False
    else:
        x, y = m.groups()
        mul = int(x) * int(y)
        mul_sum += mul
        if mul_enabled:
            accurate_mul_sum += mul


print("Part 1:", mul_sum)
print("Part 2:", accurate_mul_sum)
