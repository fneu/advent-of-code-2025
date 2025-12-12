from math import prod

with open("input12.txt") as f:
    lines = f.readlines()

total = 0
for line in lines[30:]:
    area, nums = (x.strip() for x in line.split(":"))
    if (prod(int(n) for n in area.split("x"))
            >= sum(int(n) * 9 for n in nums.split(" "))):
        total += 1
print(total)
