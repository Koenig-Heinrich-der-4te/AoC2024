with open("08.txt") as file:
    data = file.read()

node_map = {freq:[] for freq in set(data) - set(".")}
lines = data.splitlines()
size_x, size_y = len(lines[0]), len(lines)
for i in range(size_y):
    for j in range(size_x):
        if lines[i][j] != ".":
            node_map[lines[i][j]].append((j, i))


def generate_antinodes(nodes, resonant_harmonics):
    antinodes = set()
    for x0, y0 in nodes:
        for x1, y1 in nodes:
            if x0 == x1 and y0 == y1:
                continue
            i = 0 if resonant_harmonics else 1
            while resonant_harmonics or i == 1:
                anti_x = x0 + (x0 - x1) * i
                anti_y = y0 + (y0 - y1) * i
                if 0 <= anti_x < size_x and 0 <= anti_y < size_y:
                    antinodes.add((anti_x, anti_y))
                    i += 1
                else:
                    break
    return antinodes

antinodes = set()
resonant_harmonic_antinodes = set()
for freq, nodes in node_map.items():
    antinodes |= generate_antinodes(nodes, False)
    resonant_harmonic_antinodes |= generate_antinodes(nodes, True)

print("Part 1:", len(antinodes))
print("Part 2:", len(resonant_harmonic_antinodes))
