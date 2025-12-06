from math import prod

with open("input6.txt", "r") as f:
    lines = f.readlines()

problems = list(zip(*([x.strip() for x in line.split(" ") if x] for line in lines)))

total = 0
for problem in problems:
    nums = [int(x) for x in problem[:-1]]
    if problem[-1] == "*":
        total += prod(nums)
    else:
        total += sum(nums)

print(total)  # part 1

total = 0
product = True
nums = []
for i in range(max(len(line) for line in lines)+1):
    if len(lines[-1]) > i and lines[-1][i] == "*":
        product = True
    if len(lines[-1]) > i and lines[-1][i] == "+":
        product = False
    num = [line[i].replace('\n', ' ') if (len(line) > i) else " " for line in lines[:-1]]
    if all(c == " " for c in num):
        if product:
            total += prod(nums)
        else:
            total += sum(nums)
        nums = []
    else:
        nums.append(int("".join(num)))
print(total)  # part 2

