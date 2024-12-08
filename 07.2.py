with open("07.txt") as file:
    data = file.read()

def test(result, numbers, current=None):
    if current is None:
        current, *numbers = numbers
    if len(numbers) == 0:
        return current == result
    n, *remaining_numbers = numbers
    return test(result, remaining_numbers, current * n) \
        or test(result, remaining_numbers, current + n) \
        or test(result, remaining_numbers, int(str(current) + str(n)))


calibration_result = 0
for line in data.splitlines():
    result, equation = line.split(": ")
    result = int(result)
    numbers = list(map(int, equation.split()))
    if result == 7290:
        print()
    if test(result, numbers):
        calibration_result += result

print("Part 2:", calibration_result)
