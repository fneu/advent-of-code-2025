with open("input5.txt", "r") as f:
    lines = f.readlines()

split_line = 0
fresh_ranges = []

for line in lines:
    if line.strip() == "":
        break

    split_line += 1
    fresh_ranges.append([int(n) for n in line.strip().split("-")])

total_fresh = 0
for line in lines[split_line + 1:]:
    vid = int(line.strip())
    for r in fresh_ranges:
        if r[0] <= vid <= r[1]:
            total_fresh += 1
            break

print(total_fresh)  # part 1

unique_fresh = [fresh_ranges[0]]

for fr in fresh_ranges[1:]:
    new_min = fr[0]
    new_max = fr[1]
    for ur in reversed(unique_fresh):  # copy iterator
        # overlap:
        if new_min <= ur[1] and ur[0] <= new_max:
            unique_fresh.remove(ur)
            new_min, new_max =  min(ur[0], new_min), max(ur[1], new_max)
    unique_fresh.append([new_min, new_max])

print(unique_fresh)
total_unique_fresh = 0
for uf in unique_fresh:
    total_unique_fresh += (uf[1] - uf[0] + 1)

print(total_unique_fresh)  # part 2