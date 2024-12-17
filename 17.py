with open("17.txt") as file:
    data = file.read()

lines = data.splitlines()
original_registers = [int(line.split(": ")[1]) for line in lines[:3]]
program = list(map(int, lines[-1].split(": ")[1].split(",")))

REG_A = 0
REG_B = 1
REG_C = 2


def get_combo(operand, registers):
    if operand < 4:
        return operand
    return registers[operand - 4]


def execute(ptr, op_code, operand, registers, output):
    match op_code:
        case 0:  # adv
            registers[REG_A] //= 2 ** get_combo(operand, registers)
        case 1:  # bxl
            registers[REG_B] ^= operand
        case 2:  # bst
            registers[REG_B] = get_combo(operand, registers) % 8
        case 3:  # jnz
            if registers[REG_A] != 0:
                return operand
        case 4:  # bxc
            registers[REG_B] ^= registers[REG_C]
        case 5:  # out
            output(get_combo(operand, registers) % 8)
        case 6:  # bdv
            registers[REG_B] = registers[REG_A] // (2 ** get_combo(operand, registers))
        case 7:  # cdv
            registers[REG_C] = registers[REG_A] // (2 ** get_combo(operand, registers))
    return ptr + 2


def run_program(registers):
    instr_ptr = 0
    result = []
    while instr_ptr < len(program):
        instr_ptr = execute(
            instr_ptr,
            program[instr_ptr],
            program[instr_ptr + 1],
            registers,
            result.append,
        )
    return result


def find_proper_value(value, depth):
    if depth == -1:
        return value
    inc = 8**depth
    for i in range(8):
        registers = [value + i * inc] + original_registers[1:]
        result = run_program(registers)
        if result[depth] == program[depth]:
            new = find_proper_value(value + i * inc, depth - 1)
            if new is not None:
                return new
    return None


output = run_program(original_registers[:])
print("Part 1:", ",".join(map(str, output)))
index = len(program) - 1
replacement = find_proper_value(8**index, index)
print("Part 2:", replacement)
