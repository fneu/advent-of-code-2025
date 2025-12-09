import itertools

with open("input9.txt", "r") as f:
    square_lines = f.readlines()

coords = [[int(n) for n in line.split(",")] for line in square_lines]

max_area = 0
for combination in itertools.combinations(coords, 2):
    [x1, y1], [x2, y2] = combination
    area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
    if area > max_area:
        max_area = area
print(max_area)  # part 1

polygon_lines = []
for i in range(len(coords)):
    polygon_lines.append((coords[i - 1], coords[i]))

max_area = 0
for combination in itertools.combinations(coords, 2):
    [x1, y1], [x2, y2] = combination
    min_x = min(x1, x2)
    min_y = min(y1, y2)
    max_x = max(x1, x2)
    max_y = max(y1, y2)
    for p_line in polygon_lines:
        if not (
            min_x >= max(p_line[0][0], p_line[1][0])
            or max_x <= min(p_line[0][0], p_line[1][0])
            or min_y >= max(p_line[0][1], p_line[1][1])
            or max_y <= min(p_line[0][1], p_line[1][1])
        ):
            break
    else:
        area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        if area > max_area:
            max_area = area
print(max_area)  # part 2