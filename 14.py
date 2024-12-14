import re

with open("14.txt") as file:
    data = file.read()
    width = 101
    height = 103

robots = []

for match in re.finditer("p=(\-?\d+),(\-?\d+) v=(\-?\d+),(\-?\d+)", data):
    robot = list(map(int, match.groups()))
    robots.append(robot)


def simulate_second(robots):
    for i, (x, y, dx, dy) in enumerate(robots):
        new_x = (x + dx) % width
        new_y = (y + dy) % height
        robots[i] = (new_x, new_y, dx, dy)


def get_quadrant(robots, selector):
    selection = [1 for robot in robots if selector(robot[:2])]
    return len(selection)


def print_bots(robots):
    positions = {}
    for x, y, _, _ in robots:
        positions[(x, y)] = positions.get((x, y), 0) + 1
    for y in range(height):
        for x in range(width):
            print(positions.get((x, y), "."), end="")
        print()


for i in range(100):
    simulate_second(robots)


q1 = get_quadrant(robots, (lambda pos: pos[0] < width // 2 and pos[1] < height // 2))
q2 = get_quadrant(robots, (lambda pos: pos[0] > width // 2 and pos[1] < height // 2))
q3 = get_quadrant(robots, (lambda pos: pos[0] < width // 2 and pos[1] > height // 2))
q4 = get_quadrant(robots, (lambda pos: pos[0] > width // 2 and pos[1] > height // 2))

print("Part 1:", q1 * q2 * q3 * q4)
i = 100
while True:
    i += 1
    simulate_second(robots)
    positions = {}
    for x, y, _, _ in robots:
        positions[(x, y)] = positions.get((x, y), 0) + 1
    if max(positions.values()) == 1:
        break
print("Part 2: ", i)
print_bots(robots)
