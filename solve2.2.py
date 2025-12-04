with open("input2.txt", "r") as f:
    ids = [[int(n) for n in r.split("-")] for r in f.read().strip().split(",")]

maximum = max(max(id) for id in ids)
maxstr = str(maximum)

possiblemultiples = set()
for l in range(2, 11):
    for n in range(1, maximum):
        s = int(str(n)*l)
        if s > maximum:
            break
        possiblemultiples.add(s)

total = 0
for nmin, nmax in ids:
    print(nmin, nmax)
    total += sum([p for p in possiblemultiples if nmax >= p >= nmin])

print(total)