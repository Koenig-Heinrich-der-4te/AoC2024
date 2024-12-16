with open("16.txt") as file:
    data = file.read()

lines = data.splitlines()
height = len(lines)
width = len(lines[0])
walls = {(x, y) for y in range(height) for x in range(width) if lines[y][x] == "#"}
start = next((x, y) for y in range(height) for x in range(width) if lines[y][x] == "S")
end = next((x, y) for y in range(height) for x in range(width) if lines[y][x] == "E")
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def find_best_path(start):
    visted = {}
    queue = [((start[0] - 1, start[1]), (1, 0), 0, None)]
    while len(queue) > 0:
        (x, y), (dx, dy), cost, parent_id = queue.pop(0)
        x += dx
        y += dy
        if (x, y) in walls:
            continue
        cost += 1
        id = ((x, y), (dx, dy))
        if id in visted and visted[id][0] <= cost:
            if visted[id][0] == cost:
                visted[id][1].append(parent_id)
            continue
        visted[id] = (cost, [parent_id])
        queue.append(((x, y), (dx, dy), cost, id))
        queue.append(((x, y), (-dy, dx), cost + 1000, id))
        queue.append(((x, y), (dy, -dx), cost + 1000, id))
    return visted


def find_best_spots(results, start, end, score):
    queue = [
        (pos, dir)
        for (pos, dir), (s, _) in results.items()
        if pos == end and score + 1 == s
    ]

    best_positions = {start}
    while len(queue) > 0:
        key = queue.pop()
        if key is None:
            continue
        best_positions.add(key[0])
        queue.extend(results[key][1])
    return best_positions


results = find_best_path(start)
score = min(cost - 1 for (pos, _), (cost, _) in results.items() if pos == end)
print("Part 1:", score)
best_positions = find_best_spots(results, start, end, score)
print("Part 2:", len(best_positions))
