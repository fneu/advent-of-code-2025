with open("input7.txt", "r") as f:
    lines = f.readlines()

total_splits = 0
tachyon_locations = {lines[0].find("S")}
for line in lines[1:]:
    new_locations = set()
    for location in tachyon_locations:
        if line[location] == "^":
            new_locations.add(location - 1)
            new_locations.add(location + 1)
            total_splits += 1
        else:
            new_locations.add(location)
    tachyon_locations = new_locations
print(total_splits)  # part 1

total_timelines = [1 if c == "S" else 0 for c in lines[0]]
for line in lines[1:]:
    new_timelines = [0 for c in line]
    for i in range(len(line)):
        if line[i] == "^":
            new_timelines[i - 1] += total_timelines[i]
            new_timelines[i + 1] += total_timelines[i]
        else:
            new_timelines[i] += total_timelines[i]
    total_timelines = new_timelines
print(sum(total_timelines))