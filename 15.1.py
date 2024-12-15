with open("15.txt") as file:
    data = file.read()

warehouse, moves = data.split("\n\n")
warehouse = warehouse.splitlines()
height = len(warehouse)
width = len(warehouse[0])
walls = {(x, y) for y in range(height) for x in range(width) if warehouse[y][x] == "#"}
crates = {(x, y) for y in range(height) for x in range(width) if warehouse[y][x] == "O"}
robot = next(
    (x, y) for y in range(height) for x in range(width) if warehouse[y][x] == "@"
)
moves = moves.strip().replace("\n", "")

directions = {
    "<": (-1, 0),
    ">": (1, 0),
    "^": (0, -1),
    "v": (0, 1),
}


def try_move(direction, robot):
    dx, dy = direction
    x, y = robot
    new = x + dx, y + dy
    can_move = new not in walls
    if new in crates:
        can_move = False
        nx, ny = new
        while (nx, ny) in crates:
            nx += dx
            ny += dy
        if (nx, ny) not in walls:
            crates.remove(new)
            crates.add((nx, ny))
            can_move = True
    return new if can_move else robot


for move in moves:
    direction = directions[move]
    robot = try_move(direction, robot)

result = sum(y * 100 + x for x, y in crates)
print("Part 1:", result)
