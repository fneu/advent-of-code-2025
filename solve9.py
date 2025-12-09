import itertools

with open("input9.txt", "r") as f:
    square_lines = f.readlines()

coords = [[int(n) for n in line.split(",")] for line in square_lines]
polygon_lines = [(coords[i - 1], coords[i]) for i in range(len(coords))]

part_1 = 0
part_2 = 0
for square in itertools.combinations(coords, 2):
    [x1, y1], [x2, y2] = square
    area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
    part_1 = max(part_1, area)
    for p_line in polygon_lines:
        if not (
            min(x1, x2) >= max(p_line[0][0], p_line[1][0])
            or max(x1, x2) <= min(p_line[0][0], p_line[1][0])
            or min(y1, y2) >= max(p_line[0][1], p_line[1][1])
            or max(y1, y2) <= min(p_line[0][1], p_line[1][1])
        ):
            break
    else:
        part_2 = max(part_2, area)

print(part_1, part_2)
