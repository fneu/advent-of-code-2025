import numpy as np
import itertools
import sys

with open("input8.txt", "r") as f:
    lines = f.readlines()

coords = list(np.array([int(n) for n in line.split(",")]) for line in lines)
indices = range(len(coords))
connections = itertools.combinations(indices, 2)
sorted_connections = list(sorted(connections, key=lambda t: np.linalg.norm(coords[t[0]] - coords[t[1]])))

relevant = sorted_connections[:1000]
circuits = []

for conn in relevant:
    a, b = conn
    circuit_with_a = None
    circuit_with_b = None
    for i in range(len(circuits)):
        circuit = circuits[i]
        if a in circuit:
            circuit_with_a = i
        if b in circuit:
            circuit_with_b = i

    if circuit_with_a is None and circuit_with_b is None:
        circuits.append({a, b})
    elif circuit_with_a is None:
        circuits[circuit_with_b].add(a)
        circuits[circuit_with_b].add(b)
    elif circuit_with_b is None:
        circuits[circuit_with_a].add(a)
        circuits[circuit_with_a].add(b)
    elif circuit_with_b == circuit_with_a:
        continue
    else:
        merged = set.union(circuits[circuit_with_a], circuits[circuit_with_b], {a, b})
        del(circuits[max(circuit_with_a, circuit_with_b)])
        del(circuits[min(circuit_with_a, circuit_with_b)])
        circuits.append(merged)

lengths = sorted(len(c) for c in circuits)
print(lengths[-1] * lengths[-2] * lengths[-3])  # part 1

circuits = []
for conn in sorted_connections:
    a, b = conn
    circuit_with_a = None
    circuit_with_b = None
    for i in range(len(circuits)):
        circuit = circuits[i]
        if a in circuit:
            circuit_with_a = i
        if b in circuit:
            circuit_with_b = i

    if circuit_with_a is None and circuit_with_b is None:
        circuits.append({a, b})
    elif circuit_with_a is None:
        circuits[circuit_with_b].add(a)
        circuits[circuit_with_b].add(b)
    elif circuit_with_b is None:
        circuits[circuit_with_a].add(a)
        circuits[circuit_with_a].add(b)
    elif circuit_with_b == circuit_with_a:
        continue
    else:
        merged = set.union(circuits[circuit_with_a], circuits[circuit_with_b], {a, b})
        del(circuits[max(circuit_with_a, circuit_with_b)])
        del(circuits[min(circuit_with_a, circuit_with_b)])
        circuits.append(merged)

    if len(circuits[0]) == len(coords):
        print(coords[a][0] * coords[b][0])
        sys.exit()

