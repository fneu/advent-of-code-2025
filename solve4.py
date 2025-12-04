from collections import defaultdict

with open("input4.txt", "r") as f:
    chars = list(line.strip() for line in f.readlines())

grid = defaultdict(lambda: ".")
for x in range(len(chars)):
    for y in range(len(chars[0])):
        grid[(x, y)] = chars[x][y]


def num_neighbors(t):
    x, y = t
    neighbors = [
        grid[x-1, y-1],
        grid[x-1, y],
        grid[x-1, y+1],
        grid[x, y-1],
        grid[x, y+1],
        grid[x+1, y-1],
        grid[x+1, y],
        grid[x+1, y+1],
    ]
    return len(list(filter(lambda c: c == "@", neighbors)))

valid = 0
for x in range(len(chars)):
    for y in range(len(chars[0])):
        if grid[(x, y)] == "@" and num_neighbors((x, y)) < 4:
            valid += 1

print(valid)  # part 1

removed_total = 0
while True:
    removed_now = 0
    for x in range(len(chars)):
        for y in range(len(chars[0])):
            if grid[(x, y)] == "@" and num_neighbors((x, y)) < 4:
                removed_now += 1
                grid[(x, y)] = "."
    if removed_now > 0:
        removed_total += removed_now
    else:
        break

print(removed_total)  # part 2
