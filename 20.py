with open("20.txt") as file:
    data = file.read()
    min_cheats_size = 100


lines = data.splitlines()
width = len(lines[0])
height = len(lines)
obstacles = {(x, y) for y in range(height) for x in range(width) if lines[y][x] == "#"}
start = next((x, y) for y in range(height) for x in range(width) if lines[y][x] == "S")
end = next((x, y) for y in range(height) for x in range(width) if lines[y][x] == "E")
direcions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def determine_distances():
    positions = {end: 0}
    queue = [(end, 0)]
    while len(queue) > 0:
        (x, y), dist = queue.pop(0)
        for dx, dy in direcions:
            pos = (x + dx, y + dy)
            if pos in obstacles or positions.get(pos, 1e10) <= dist + 1:
                continue
            queue.append((pos, dist + 1))
            positions[pos] = dist + 1
    return positions


def find_cheats(pos, depth):
    visited = {pos: 0}
    cheats = {}
    queue = [(pos, 0)]
    while len(queue):
        (x, y), d = queue.pop(0)
        for dx, dy in direcions:
            p = (x + dx, y + dy)
            if not (0 <= p[0] < width and 0 <= p[1] < height):
                continue
            if p in visited and visited[p] <= d + 1:
                continue
            if p not in obstacles:
                cheats[p] = d + 1
            if d + 1 < depth:
                queue.append((p, d + 1))
                visited[p] = d + 1

    return cheats.items()


distances = determine_distances()


def get_cheat_count(cheat_duration):
    cheat_count = 0
    for pos, d in distances.items():
        for cp, length in find_cheats(pos, cheat_duration):
            cheatsize = d - length - distances[cp]
            if cheatsize >= min_cheats_size:
                cheat_count += 1
    return cheat_count


print("Part 1:", get_cheat_count(2))
print("Part 2:", get_cheat_count(20))
