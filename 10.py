with open("10.txt") as file:
    data = file.read()


grid = [list(map(int, line)) for line in data.splitlines()]

size_x = len(grid[0])
size_y = len(grid)


def get(x, y):
    if 0 <= x < size_x and 0 <= y < size_y:
        return grid[y][x]
    return -1


def get_trail_heads():
    for x in range(size_x):
        for y in range(size_y):
            if get(x, y) == 0:
                yield x, y


def explore(trailhead):
    tx, ty = trailhead
    destinations = set()
    heads = [(tx, ty, 0)]
    trails_count = 0
    while len(heads) > 0:
        x, y, n = heads.pop()
        if n == 9:
            destinations.add((x, y))
            trails_count += 1
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            height = get(x + dx, y + dy)
            if height - n == 1:
                heads.append((x + dx, y + dy, height))
    return len(destinations), trails_count


reachable_destinations = 0
distinct_trails = 0
for trailhead in get_trail_heads():
    reachable, path_count = explore(trailhead)
    reachable_destinations += reachable
    distinct_trails += path_count

print("Part 1:", reachable_destinations)
print("Part 2:", distinct_trails)
