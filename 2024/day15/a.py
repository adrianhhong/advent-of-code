og_grid, m =  open(0).read().split('\n\n')

grid = []
commands = []
robot = []

for i, s in enumerate(og_grid.splitlines()):
    l = list(s)
    for j, c in enumerate(l):
        if c == "@":
            robot = [i, j]
    grid.append(l)

for l in m:
    commands += l.split()


def push(x, y, dir, grid):
    next_x, next_y = x, y
    while True:
        # look at next spot
        next_x += dir[0]
        next_y += dir[1]
        if grid[next_x][next_y] == "#":
            # can't be pushed, there's a back wall
            return False
        elif grid[next_x][next_y] == ".":
            # can be pushed, empty space
            grid[next_x][next_y] = "O"
            grid[x][y] = "."
            grid[x+dir[0]][y+dir[1]] = "@"
            return True
        


directions = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1)
}

for c in commands:
    d = directions[c]
    # look at what is in the next spot
    x = robot[0] + d[0]
    y = robot[1] + d[1]
    if grid[x][y] == ".":
        grid[robot[0]][robot[1]] = "."
        grid[x][y] = "@"
        robot = [x,y]
    elif grid[x][y] == "#":
        continue
    elif grid[x][y] == "O":
        if push(robot[0], robot[1], d, grid):
            robot = [x,y]
    

for r in grid:
    print(r)

t = 0 
for i in range(len(grid)):
    for j in range(len(grid[i])) :
        if grid[i][j] == "O":
            t += i * 100 + j

print(t)
