with open("18.txt") as file:
    data = file.read()

size = 71
start = (0, 0)
target = (70, 70)

initial_amount = 1024

bytes = [tuple(map(int, line.split(","))) for line in data.splitlines()]
direcions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def path_find(start, finish, obstacles, bounds):
    locations = {start: (0, None)}
    queue = [(start, 0)]
    best = int(1e10)
    while len(queue) > 0:
        (x, y), cost = queue.pop(0)
        if (x, y) == finish:
            best = min(best, cost)
        if cost >= best or locations[(x, y)][0] < cost:
            continue
        for dx, dy in direcions:
            pos = (x + dx, y + dy)
            if pos in obstacles:
                continue
            if not (0 <= pos[0] < bounds[0] and 0 <= pos[1] < bounds[1]):
                continue
            if pos in locations and locations[pos][0] <= cost + 1:
                continue
            locations[pos] = (cost + 1, (x, y))
            queue.append((pos, cost + 1))

    if finish not in locations:
        return None

    path = []
    node = finish
    while node is not None:
        path.append(node)
        _, node = locations[node]

    return path


obstacles = set(bytes[:initial_amount])

path = path_find(start, target, obstacles, (size, size))
print("Part 1:", len(path) - 1)

path_positions = set(path)

for pos in bytes[initial_amount:]:
    obstacles.add(pos)
    if pos in path_positions:
        path = path_find(start, target, obstacles, (size, size))
        if path is None:
            break
        path_positions = set(path)

print(f"Part 2: {pos[0]},{pos[1]}")
