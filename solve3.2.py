with open("input3.txt", "r") as f:
    lines = f.readlines()

banks = map(lambda _line: [int(x) for x in _line.strip()], lines)
joltage = 0

for bank in banks:
    result = 0
    last_index = -1
    for digits_left in range(11, -1, -1):
        valid_bank = bank[last_index + 1: -1 * digits_left if digits_left else None]
        max_valid = max(valid_bank)
        last_index = valid_bank.index(max_valid) + last_index + 1
        result = result * 10 + max_valid

    joltage += result
print(joltage)