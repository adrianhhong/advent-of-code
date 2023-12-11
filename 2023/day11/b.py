import numpy as np
from collections import deque as queue


grid = []

lines = open("input.txt").read().split('\n')
for i, l in enumerate(lines):
    grid.append(list(l))

expand_x = []
expand_y = []

# find all empty rows and cols
for i in range(len(grid)):
    has_galaxy = False
    for j in range(len(grid[0])):
        if grid[i][j] == "#":
            has_galaxy = True
            break
    if not has_galaxy:
        expand_x.append(i)

for j in range(len(grid[0])):
    has_galaxy = False
    for i in range(len(grid)):
        if grid[i][j] == "#":
            has_galaxy = True
            break
    if not has_galaxy:
        expand_y.append(j)
            

galaxy_coords = []

# find coordinates of all galaxies
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "#":
            galaxy_coords.append((i, j))

# print(galaxy_coords)

total_dist = 0

# find distance between all galaxies. if we hit an empty row or col, add 1000000-1
for i, g1 in enumerate(galaxy_coords):
    for j in range(i+1, len(galaxy_coords)):
        g2 = galaxy_coords[j]
        num_ex = 0
        for ex in expand_x:
            if min(g2[0], g1[0]) < ex < max(g2[0], g1[0]):
                num_ex += 1
        x_dist = abs(g2[0] - g1[0]) + num_ex*(1000000-1)
        num_ey = 0
        for ey in expand_y:
            if min(g2[1], g1[1]) < ey < max(g2[1], g1[1]):
                num_ey += 1
        y_dist = abs(g2[1] - g1[1]) + num_ey*(1000000-1)
        # print("stats", g1, g2, x_dist, y_dist, num_ex, num_ey)
        total_dist += (x_dist + y_dist)

print(total_dist)