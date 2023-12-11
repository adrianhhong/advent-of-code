import re

total = 0
grid = []

with open('input.txt') as input:
    for i, line in enumerate(input):
        grid.append(list(line.rstrip()))


grid_l_last_ind = len(grid) - 1
grid_w_last_ind = len(grid[0])-1

def is_symbol(char):
    if (re.search(r'\d|\.', char)):
        return False
    return True

def has_adjacent_symbol(grid, line_i, start_i, end_i):
    print(line_i, start_i, end_i)
    for i in range(line_i-1, line_i+2):
        if (i < 0 or i > grid_l_last_ind): # If out of bounds, go next.
            continue
        for j in range(start_i-1, end_i+2):
            print(i,j)
            if (j < 0 or j > grid_w_last_ind): # If out of bounds, go next.
                continue
            if is_symbol(grid[i][j]):
                print('YES')
                return True




for i, line in enumerate(grid):
    curr_num = ""
    for j, char in enumerate(line):
        if not char.isnumeric() and curr_num != '': # Reach end of number
            print("curr_num", curr_num)
            if has_adjacent_symbol(grid, i, j-len(curr_num), j-1):
                total += int(curr_num)
                print("total", total)
            curr_num = ''
        if char.isnumeric():
            curr_num += char
            if j is grid_w_last_ind: # Reach end of line
                print("curr_num", curr_num)
                if has_adjacent_symbol(grid, i, j-len(curr_num), j-1):
                    total += int(curr_num)
                    print("total", total)
                curr_num = ''

        



print(total)
