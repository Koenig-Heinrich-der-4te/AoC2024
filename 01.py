with open("01.txt") as file:
    data = file.read()

rows = [line.split("   ") for line in data.split("\n")]
left = [int(row[0]) for row in rows]
right = [int(row[1]) for row in rows]

left.sort()
right.sort()

total_distance = sum(abs(a - b) for a, b in zip(left, right))
print("Part 1: ", total_distance)

left = {n: left.count(n) for n in set(left)}
right = {n: right.count(n) for n in set(right)}

similarity_score = 0

for n, count in left.items():
    similarity_score += n * count * right.get(n, 0)

print("Part 2:", similarity_score)
