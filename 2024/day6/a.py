input = open(0).read().splitlines()

grid = []
loc = []
curr_dir = "^"
for ri, row in enumerate(input):
    if "^" in row:
        loc = [ri, row.index("^")]
    grid.append(list(row))

dir = { "^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
dir_order = "^>v<"
next_r = loc[0] + dir[curr_dir][0]
next_c = loc[1] + dir[curr_dir][1]

while -1 < next_r < len(grid) and -1 < next_c < len(grid[0]):

    # for r in grid:
    #     print(r)
    grid[loc[0]][loc[1]] = "o"

    next_symbol = grid[next_r][next_c]
    # print(next_r, next_c)

    if next_symbol is "#":
        curr_dir = dir_order[(dir_order.index(curr_dir) + 1) % len(dir_order)]
        next_r = loc[0] + dir[curr_dir][0]
        next_c = loc[1] + dir[curr_dir][1]
        grid[next_r][next_c] = curr_dir
    else:
        grid[next_r][next_c] = curr_dir

    loc = [next_r, next_c]
    next_r = loc[0] + dir[curr_dir][0]
    next_c = loc[1] + dir[curr_dir][1]
    for r in grid:
        print(r)
    
t=0
for r in grid:
    for c in r:
        if c == 'o':
            t+=1

print(loc)
print(t+1)
