input = open("input.txt").read().split('\n')
dirs = []
amounts = []

direction_conversion = ["R", "D", "L", "U"]

for l in input:
    a, b, rest = l.split(' ')
    col = rest.split("(#")[1].split(")")[0]
    dirs.append(direction_conversion[int(col[5])])
    amounts.append(int(col[0:5], 16))

direction_array = ["U", "R", "D", "L"]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x, y = 0, 0
points = [(x,y)]
perimeter = 0

for i, d in enumerate(dirs):
    direction_index = direction_array.index(d)
    amount = amounts[i]
    x = x + dx[direction_index] * amount
    y = y + dy[direction_index] * amount
    points.append((x, y))
    perimeter += amount

# shoelace theorem
area_inside = 0
for i in range(len(points)- 1):
    area_inside += (points[i][1]+points[i+1][1]) * (points[i][0] - points[i+1][0])
shoelace_inside = abs(area_inside // 2)

# pick's formula
print(shoelace_inside + perimeter // 2 + 1)