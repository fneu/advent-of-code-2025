from tqdm import tqdm

with open("input1.txt", "r") as f:
    lines = f.readlines()

dial = range(100)
index = 50
count = 0

for line in tqdm(lines):
    c, num = line[0], int(line[1:])
    if c == "R":
        index = (index + num) % 100
    else:
        index = (index - num) % 100

    if dial[index] == 0:
        count += 1

print(count)
index = 50
count = 0

for line in tqdm(lines):
    c, num = line[0], int(line[1:])
    old = dial[index]
    count += num // 100

    if c == "R":
        index = (index + num) % 100
        if dial[index] == 0 or dial[index] < old != 0:
            count += 1
    else:
        index = (index - num) % 100
        if dial[index] == 0 or dial[index] > old != 0:
            count += 1

print(count)