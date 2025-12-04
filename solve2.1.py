with open("input2.txt", "r") as f:
    ids = [[int(n) for n in r.split("-")] for r in f.read().strip().split(",")]

maximum = max(max(id) for id in ids)
maxstr = str(maximum)
assert(len(maxstr) % 2 == 0)

maxpair = int(maxstr[:len(maxstr)//2])
possiblepairs = [int(f"{s}{s}") for s in range(1, maxpair)]

total = 0
for nmin, nmax in ids:
    total += sum([p for p in possiblepairs if nmax >= p >= nmin])

print(total)
