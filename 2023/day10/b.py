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

checked_grid = np.full((len(grid), len(grid[0])), 0)
checked_grid[curr_row][curr_col] = 1


def direction_valid(curr_symbol, next_symbol, direction):
    # print(curr_symbol, next_symbol, direction)
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
    return checked_grid[row][col] != 0

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
            checked_grid[adjx][adjy] = 1
            q.append((adjx, adjy))

import sys
np.set_printoptions(threshold=sys.maxsize)

print(grid)
print(checked_grid)
# print(np.max(checked_grid))

total = 0

# going from left to right, if odd it's inside, if even it's outside https://en.wikipedia.org/wiki/Point_in_polygon
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if checked_grid[i][j] != 1:
            # for this coord that is not part of the main loop, check how many walls we hit in that row. odd = we are inside, even = we are outside
            inside_num =0 
            for y in range(j+1, len(grid[0])):
                if checked_grid[i][y] and grid[i][y] in "|7F": # F--J we are still inside so count only F. same with L--7. L--J we are outside, so need to count neither or both. same with F--7
                    # hardcoded out "S" since S will be a J piece
                    inside_num += 1
            total += 1 if inside_num % 2 == 1 else 0
            print(i,j, inside_num, total)


print(total)


