with open("06.txt") as file:
    data = file.read()

lines = data.splitlines()
max_x = len(lines[0])
max_y = len(lines)

obstacles = {(x, y) for y in range(max_y) for x in range(max_x) if lines[y][x] == "#"}
start = data.index("^")
line_len = (len(lines[0]) + 1)
start = (start % line_len, start // line_len)

def walk(start, obstacles):
    x, y = start
    dx, dy = 0, -1
    recorded_steps = set()
    looping = False
    while 0 <= x < max_x and 0 <= y < max_y and not looping:
        pos = ((x, y), (dx, dy))
        looping = pos in recorded_steps
        recorded_steps.add(pos)
        while (x + dx, y + dy) in obstacles:
            dx, dy = -dy, dx
        x, y = x + dx, y + dy
    return recorded_steps, looping

steps, _ = walk(start, obstacles)
actual_positions = {pos for pos, _ in steps}
print("Part 1:", len(actual_positions))

print("Part 2 may take a few seconds")

actual_positions.remove(start)
looping_obstacles = 0
for pos in actual_positions:
    obstacles.add(pos)
    _, looping = walk(start, obstacles)
    obstacles.remove(pos)
    looping_obstacles += looping

print("Part 2:", looping_obstacles)