import re

total = 0
grid = []
stars= {} # {"i-j": {location: [i,j], surr_n: [1,2,3,etc.]}}

with open('input.txt') as input:
    for i, line in enumerate(input):
        grid.append(list(line.rstrip()))


grid_l_last_ind = len(grid) - 1
grid_w_last_ind = len(grid[0])-1

def is_star(char):
    if (re.search(r'\*', char)):
        return True

def has_adjacent_star(grid, line_i, start_i, end_i, curr_num):
    for i in range(line_i-1, line_i+2):
        if (i < 0 or i > grid_l_last_ind): # If out of bounds, go next.
            continue
        for j in range(start_i-1, end_i+2):
            if (j < 0 or j > grid_w_last_ind): # If out of bounds, go next.
                continue
            if is_star(grid[i][j]):
                if f"{i}-{j}" in stars:
                    stars[f"{i}-{j}"]["surr_n"].append(int(curr_num))
                else:
                    stars[f"{i}-{j}"] = {"location": [i,j], "surr_n": [int(curr_num)]}

for i, line in enumerate(grid):
    curr_num = ""
    for j, char in enumerate(line):
        if not char.isnumeric() and curr_num != '': # Reach end of number
            has_adjacent_star(grid, i, j-len(curr_num), j-1, curr_num)
            curr_num = ''
        if char.isnumeric():
            curr_num += char
            if j is grid_w_last_ind: # Reach end of line
                has_adjacent_star(grid, i, j-len(curr_num), j-1, curr_num)
                curr_num = ''

        

for star in stars.values():
    if len(star['surr_n']) == 2:
        total += (star['surr_n'][0] * star['surr_n'][1])

print(total)
