import re

# size = (11,7)
size = (101,103)

t = 0

def wrap(x,y):
    x = x % size[0]
    y = y % size[1]
    return x, y

q1, q2, q3, q4 = 0, 0, 0, 0

for l in open(0).read().splitlines():
    x, y, vx, vy = list(map(int, re.findall(r"-?\d+", l)))
    x += 100*vx
    y += 100*vy
    x, y = wrap(x,y)

    if 0 <= x < (size[0] // 2) and 0 <= y < (size[1] // 2):
        q1 += 1
    if (size[0] // 2) < x < size[0] and 0 <= y < (size[1] // 2):
        q2 += 1
    if 0 <= x < (size[0] // 2) and (size[1] // 2) < y < size[1]:
        q3 += 1
    if (size[0] // 2) < x < size[0] and (size[1] // 2) < y < size[1]:
        q4 += 1

print(q1*q2*q3*q4)