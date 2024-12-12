with open("12.txt") as file:
    data = file.read()

lines = data.splitlines()
types = {
    crop: set(
        (x, y) for y, line in enumerate(lines) for x, t in enumerate(line) if t == crop
    )
    for crop in set(data)
}

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def flood_collect(tiles: set):
    start = next(iter(tiles))
    collected = {start}
    tiles.remove(start)
    queue = [start]
    while len(queue) != 0:
        x, y = queue.pop()
        for dx, dy in dirs:
            pos = x + dx, y + dy
            if pos in tiles:
                collected.add(pos)
                tiles.remove(pos)
                queue.append(pos)
    return collected


def find_perimeter(tiles: set):
    perimeter = 0
    for x, y in tiles:
        for dx, dy in dirs:
            pos = x + dx, y + dy
            if pos not in tiles:
                perimeter += 1
    return perimeter


def find_sides(tiles: set):
    sides = {}

    for x, y in tiles:
        for dx, dy in dirs:
            pos = x + dx, y + dy
            if pos not in tiles:
                side = (pos[0] * dx, pos[1] * dy)
                if side not in sides:
                    sides[side] = {pos}
                else:
                    sides[side].add(pos)
    side_count = 0
    for side_tiles in sides.values():
        while len(side_tiles) != 0:
            side_count += 1
            flood_collect(side_tiles)

    return side_count


price = 0
discounted_price = 0

for crop, tiles in types.items():
    while len(tiles) != 0:
        region = flood_collect(tiles)
        size = len(region)
        perimeter = find_perimeter(region)
        price += perimeter * size
        sides = find_sides(region)
        discounted_price += sides * size

print("Part 1:", price)
print("Part 2:", discounted_price)
