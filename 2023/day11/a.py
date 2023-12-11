import numpy as np
from collections import deque as queue


grid = []

lines = open("input.txt").read().split('\n')
for i, l in enumerate(lines):
    grid.append(list(l))

print(grid)


expand_x = []
expand_y = []

# find empty rows
for i in range(len(grid)):
    has_galaxy = False
    for j in range(len(grid[0])):
        if grid[i][j] == "#":
            has_galaxy = True
            break
    if not has_galaxy:
        expand_x.append(i)

# find empty cols
for j in range(len(grid[0])):
    has_galaxy = False
    for i in range(len(grid)):
        if grid[i][j] == "#":
            has_galaxy = True
            break
    if not has_galaxy:
        expand_y.append(j)
            

print(expand_x, expand_y)

# add in an extra row/col for every empty
for i, x in enumerate(expand_x):
    grid.insert(x+i, ["."]*len(grid[0]))

for j, y in enumerate(expand_y):
    for i in range(len(grid)):
        grid[i].insert(y+j, ".")

print(grid)

galaxy_coords = []

# find where all the "#" are
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "#":
            galaxy_coords.append((i, j))

print(galaxy_coords)

total_dist = 0

# find distance between all galaxies
for i, g1 in enumerate(galaxy_coords):
    for j in range(i+1, len(galaxy_coords)):
        g2 = galaxy_coords[j]  
        x_dist = abs(g2[0] - g1[0])
        y_dist = abs(g2[1] - g1[1])
        print(g1, g2, x_dist, y_dist)
        total_dist += (x_dist + y_dist)

print(total_dist)