with open("09.txt") as file:
    data = file.read()

disc = []
for i, (blocks, spaces) in enumerate(zip(data[::2], data[1::2] + "0")):
    disc += [i] * int(blocks) + [None] * int(spaces)

insertion_index = 0
index = len(disc)


while index >= insertion_index:
    index -= 1
    if disc[index] is None:
        continue
    n = disc[index]
    disc[index] = None
    while disc[insertion_index] is not None:
        insertion_index += 1
    i = min(insertion_index, index)
    disc[i] = n


result = 0
for i, n in enumerate(disc[:insertion_index]):
    result += i * n

print("Part 1:", result)
