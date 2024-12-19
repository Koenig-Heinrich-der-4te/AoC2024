from functools import cache

with open("19.txt") as file:
    data = file.read()

patterns, wanted = data.split("\n\n")
patterns = patterns.split(", ")
wanted = wanted.splitlines()
patterns = {
    letter: [p for p in patterns if p.startswith(letter)]
    for letter in set(p[0] for p in patterns)
}


@cache
def count_arangements(combo: str):
    if len(combo) == 0:
        return 1
    count = 0
    for p in patterns.get(combo[0], ()):
        if combo.startswith(p):
            count += count_arangements(combo[len(p) :])
    return count


possible_count = 0
possbile_arangements = 0
for combination in wanted:
    arangements_count = count_arangements(combination)
    if arangements_count > 0:
        possible_count += 1
    possbile_arangements += arangements_count

print("Part 1:", possible_count)
print("Part 2:", possbile_arangements)
