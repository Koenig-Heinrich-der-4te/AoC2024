with open("15.txt") as file:
    data = file.read()

warehouse, moves = data.split("\n\n")
warehouse = warehouse.splitlines()
height = len(warehouse)
width = len(warehouse[0])
walls = {
    (2 * x + d, y)
    for y in range(height)
    for x in range(width)
    if warehouse[y][x] == "#"
    for d in range(2)
}
crates = {
    (2 * x, y) for y in range(height) for x in range(width) if warehouse[y][x] == "O"
}
robot = next(
    (2 * x, y) for y in range(height) for x in range(width) if warehouse[y][x] == "@"
)
moves = moves.strip().replace("\n", "")

directions = {
    "<": (-1, 0),
    ">": (1, 0),
    "^": (0, -1),
    "v": (0, 1),
}


def get_create_at(x, y):
    if (x, y) in crates:
        return (x, y)
    if (x - 1, y) in crates:
        return (x - 1, y)
    return None


def can_move_crate(crate, dir):
    if crate is None:
        return True
    x, y = crate
    dx, dy = dir
    for d in range(2):
        if (x + d + dx, y + dy) in walls:
            return False
        in_way = get_create_at(x + d + dx, y + dy)
        if in_way != crate and not can_move_crate(in_way, dir):
            return False
    return True


def move_crate(crate, dir):
    if crate is None:
        return
    x, y = crate
    dx, dy = dir
    crates.remove(crate)
    for d in range(2):
        in_way = get_create_at(x + d + dx, y + dy)
        move_crate(in_way, dir)
    crates.add((x + dx, y + dy))
    return True


def try_move(direction, robot):
    dx, dy = direction
    x, y = robot
    new = x + dx, y + dy
    can_move = new not in walls
    crate_in_way = get_create_at(*new)
    if crate_in_way is not None:
        can_move = can_move_crate(crate_in_way, direction)
        if can_move:
            move_crate(crate_in_way, direction)

    return new if can_move else robot


def test():
    for y in range(height):
        skip_next = False
        for x in range(width * 2):
            if skip_next:
                skip_next = False
                continue
            if (x, y) in walls:
                print("#", end="")
            elif (x, y) in crates:
                print("[]", end="")
                skip_next = True
            elif (x, y) == robot:
                print("@", end="")
            else:
                print(".", end="")
        print()


for move in moves:
    direction = directions[move]
    robot = try_move(direction, robot)

test()

result = sum(y * 100 + x for x, y in crates)
print("Part 2:", result)
