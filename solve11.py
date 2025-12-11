from functools import cache

with open("input11.txt") as f:
    lines = f.readlines()

descendants = {"out": []}
for line in lines:
    words = line.split()
    descendants[words[0][:-1]] = words[1:]


@cache
def n_paths(start, finish):
    if start == finish:
        return 1
    return sum(n_paths(child, finish) for child in descendants[start])


print(n_paths("you", "out"))

print(
    n_paths("svr", "fft") * n_paths("fft", "dac") * n_paths("dac", "out")
    + n_paths("svr", "dac") * n_paths("dac", "fft") * n_paths("fft", "out")
)
