# detail the points where he turned, if 4 points repeat more than once then it's a loop
import copy

input = open(0).read().splitlines()

grid = []

loc = []
for ri, row in enumerate(input):
    if "^" in row:
        loc = [ri, row.index("^")]
    grid.append(list(row))


dir = { "^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
dir_order = "^>v<"





def is_loop(turns):
    if len(turns) > 1000:
        return True
    return False
    # if len(turns) < 9:
    #     return False

    # for i in range(4):
    #     print(turns)
    #     print(i, turns[len(turns) - i -1], turns[len(turns) - i - 5 -1])
    #     if turns[len(turns) - i -1] != turns[len(turns) - i - 4 -1]:
    #         check_four = False

    # return True

t=0

def check_any_loops(grid, loc):
    
    curr_dir = "^"

    turns = []

    next_r = loc[0] + dir[curr_dir][0]
    next_c = loc[1] + dir[curr_dir][1]
    while -1 < next_r < len(grid) and -1 < next_c < len(grid[0]):

        # for r in grid:
        #     print(r)
        # grid[loc[0]][loc[1]] = "o"

        next_symbol = grid[next_r][next_c]
        # print(next_r, next_c)

        if next_symbol == "#":
            turns.append([loc[0], loc[1]])
            curr_dir = dir_order[(dir_order.index(curr_dir) + 1) % len(dir_order)]
            next_r = loc[0] + dir[curr_dir][0]
            next_c = loc[1] + dir[curr_dir][1]
            next_symbol = grid[next_r][next_c]
            if next_symbol == "#":
                turns.append([loc[0], loc[1]])
                curr_dir = dir_order[(dir_order.index(curr_dir) + 1) % len(dir_order)]
                next_r = loc[0] + dir[curr_dir][0]
                next_c = loc[1] + dir[curr_dir][1]
            grid[next_r][next_c] = curr_dir
        else:
            grid[next_r][next_c] = curr_dir

        loc = [next_r, next_c]
        next_r = loc[0] + dir[curr_dir][0]
        next_c = loc[1] + dir[curr_dir][1]
        if is_loop(turns):
            return True
    return False

    
# print(grid)

for ri, r in enumerate(grid):
    for ci, c in enumerate(r):
        if c == "#":
            continue
        else:
            new_grid = copy.deepcopy(grid)
            new_grid[ri][ci] = "#"
            # # print('------------')
            # for r in new_grid:
            #     print(r)
            if check_any_loops(new_grid, loc):
                # print(t)
                t+=1


check_any_loops(grid,loc)


print(t)
