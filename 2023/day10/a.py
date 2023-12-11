import numpy as np
from collections import deque as queue


grid = []
curr_col = 0
curr_row = 0

lines = open("input.txt").read().split('\n')
for i, l in enumerate(lines):
    grid.append(list(l))
    if "S" in l:
        curr_col = l.index("S")
        curr_row = i

checked_grid = np.full((len(grid), len(grid[0])), -1)
checked_grid[curr_row][curr_col] = 0


def direction_valid(curr_symbol, next_symbol, direction):
    print(curr_symbol, next_symbol, direction)
    if direction == "N" and (curr_symbol == "|" or curr_symbol == "L" or curr_symbol == "J" or curr_symbol == "S"):
        if next_symbol == "|" or next_symbol == "7" or next_symbol == "F":
            return True
        return False
    if direction == "E" and (curr_symbol == "-" or curr_symbol == "L" or curr_symbol == "F" or curr_symbol == "S"):
        if next_symbol == "-" or next_symbol == "J" or next_symbol == "7":
            return True
        return False
    if direction == "S" and (curr_symbol == "|" or curr_symbol == "7" or curr_symbol == "F" or curr_symbol == "S"):
        if next_symbol == "|" or next_symbol == "L" or next_symbol == "J":
            return True
        return False
    if direction == "W" and (curr_symbol == "-" or curr_symbol == "7" or curr_symbol == "J" or curr_symbol == "S"):
        if next_symbol == "-" or next_symbol == "F" or next_symbol == "L":
            return True
        return False

def has_visited(row, col):
    return checked_grid[row][col] != -1

# Direction vectors N, E, S, W
d = ["N", "E", "S", "W"]
dRow = [ -1, 0, 1, 0]
dCol = [ 0, 1, 0, -1]

q = queue()
q.append((curr_row, curr_col))

while len(q) > 0:
    cell = q.popleft()
    x = cell[0]
    y = cell[1]

    for i in range(4):
        adjx = x + dRow[i]
        adjy = y + dCol[i]

        if 0 <= adjx < len(grid) and 0 <= adjy < len(grid[0]) and not has_visited(adjx, adjy) and direction_valid(grid[x][y], grid[adjx][adjy], d[i]):
            checked_grid[adjx][adjy] = checked_grid[x][y] + 1
            q.append((adjx, adjy))

import sys
np.set_printoptions(threshold=sys.maxsize)

print(checked_grid)
print(np.max(checked_grid))