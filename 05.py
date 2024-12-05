with open("05.txt") as file:
    data = file.read()

raw_rules, books = data.split("\n\n")
rules = {}
for rule in raw_rules.splitlines():
    start, end = (int(n) for n in rule.split("|"))
    if start in rules:
        rules[start].append(end)
    else:
        rules[start] = [end]


def find_mistake(book):
    pages = set()
    for i, page in enumerate(book):
        for n in rules.get(page, ()):
            if n in pages:
                return (book.index(n), i)
        pages.add(page)
    return None


correct_middle_pages_sum = 0
fixed_middle_pages_sum = 0

for book in books.splitlines():
    book = [int(page) for page in book.split(",")]
    mistake = find_mistake(book)
    if mistake is None:
        correct_middle_pages_sum += book[len(book) // 2]
    else:
        while mistake is not None:
            a, b = mistake
            book[a], book[b] = book[b], book[a]
            mistake = find_mistake(book)
        fixed_middle_pages_sum += book[len(book) // 2]

print("Part 1:", correct_middle_pages_sum)
print("Part 2:", fixed_middle_pages_sum)
