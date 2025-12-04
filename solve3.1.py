with open("input3.txt", "r") as f:
    lines = f.readlines()

banks = map(lambda _line: [int(x) for x in _line.strip()], lines)
joltage = 0

for bank in banks:
    first_digit = max(bank[:-1])
    first_location = bank.index(first_digit)
    second_digit = max(bank[first_location+1:])
    result = first_digit * 10 + second_digit
    joltage += result

print(joltage)