with open("09.txt") as file:
    data = file.read()

disc = []
for i, (blocks, spaces) in enumerate(zip(data[::2], data[1::2] + "0")):
    if blocks == "0":
        disc[-1] = (None, disc[-1][1] + int(spaces))
    else:
        disc.append((i, int(blocks)))
        disc.append((None, int(spaces)))


for j in range(i, 1, -1):
    position, length = next(
        (pos, len) for (pos, (value, len)) in enumerate(disc) if value == j
    )
    for k in range(position):
        val, size = disc[k]
        if val is None and size >= length:
            disc[k] = (None, size - length)
            block = disc[position]
            spaces = length
            if position + 1 < len(disc) and disc[position + 1][0] is None:
                spaces += disc[position + 1][1]
                del disc[position + 1]
            if disc[position - 1][0] is None:
                spaces += disc[position - 1][1]
                disc[position - 1] = (None, spaces)
                del disc[position]
            else:
                disc[position] = (None, spaces)
            disc.insert(k, block)
            break


index = 0
result = 0
for value, length in disc:
    if value is None:
        index += length
        continue
    for _ in range(length):
        result += index * value
        index += 1

print("Part 2:", result)
