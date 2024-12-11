with open("11.txt") as file:
    data = file.read()


def get_next_stones(stone):
    if stone == 0:
        return [1]
    rep = str(stone)
    if len(rep) % 2 == 0:
        return [int(rep[: len(rep) // 2]), int(rep[len(rep) // 2 :])]
    return [stone * 2024]


def blink_n_times(stones, blink_amount):
    for i in range(blink_amount):
        new_stones = {}
        for stone, count in stones.items():
            for new_stone in get_next_stones(stone):
                new_stones[new_stone] = new_stones.get(new_stone, 0) + count
        stones = new_stones
    return stones


stones = {int(stone): 1 for stone in data.split()}
stones = blink_n_times(stones, 25)
print("Part 1:", sum(stones.values()))

stones = blink_n_times(stones, 50)
print("Part 2:", sum(stones.values()))
