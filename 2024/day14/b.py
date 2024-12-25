import time
import re

size = (101,103)

t = 0

def wrap(x,y):
    x = x % size[0]
    y = y % size[1]
    return x, y

def christ_tree(left, right):
    for l in left:
        if l not in right:
            return False
    return True


robots = []

for l in open(0).read().splitlines():
    robots.append(list(map(int, re.findall(r"-?\d+", l))))

while True:
    t += 1
    for i in range(len(robots)):
        new_x, new_y = wrap(robots[i][0] + robots[i][2], robots[i][1] + robots[i][3])
        robots[i] = [new_x, new_y, robots[i][2], robots[i][3]]
    
    grid = []
    if (t - 99) % 101 == 0: # when printing output, I noticed there was some vertical pattern every 101 iterations starting at 99. Eventually the christmas tree showed.
        for _i in range(size[1]):
            grid.append(['\033[95m' + "." +'\033[95m'] * size[0])
        for r in robots:
            grid[r[1]][r[0]] = '\033[92m' + "*" + '\033[92m'
        for r in grid:
            print("".join(r))
        print("\n\n\n")
        print(t)
        time.sleep(0.5)
