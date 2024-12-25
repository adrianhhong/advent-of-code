import copy

og_grid, m =  open(0).read().split('\n\n')

grid = []
commands = []
robot = []

for s in og_grid.splitlines():
    l = list(s)
    new_l = []
    for c in l:
        if c == "#":
            new_l.append("#")
            new_l.append("#")
        if c == "O":
            new_l.append("[")
            new_l.append("]")
        if c == ".":
            new_l.append(".")
            new_l.append(".")
        if c == "@":
            new_l.append("@")
            new_l.append(".")
    grid.append(new_l)


for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "@":
            robot = [i, j]


for l in m:
    commands += l.split()


def push(robot_x, robot_y, command, grid):
    visited = []
    boxes_behind_to_update = []
    new_grid = copy.deepcopy(grid)
    new_grid[robot_x][robot_y] = "."
    dir = directions[command]
    boxes = [(robot_x, robot_y, "@")]
    while len(boxes) != 0:
        box = boxes.pop()
        if box in visited:
            continue
        curr_x, curr_y, object_behind = box
        # look at next spot
        x = curr_x + dir[0]
        y = curr_y + dir[1]
        if grid[x][y] == "#":
            # can't be pushed, there's a back wall
            return False
        elif grid[x][y] == ".":
            # can be pushed, empty space
            new_grid[x][y] = object_behind
            continue
        # if we see part of a box
        boxes.append((x,y,grid[x][y]))
        # update the new_grid with the object that pushed me
        new_grid[x][y] = object_behind
        # check the other side of the box
        if grid[x][y] in ["[", "]"] and command in ["^", "v"]:
            look_x = x + box_lookaround_directions[grid[x][y]][0]
            look_y = y + box_lookaround_directions[grid[x][y]][1]
            boxes.append((look_x, look_y, grid[look_x][look_y]))
            opp = opposite_directions[command]
            boxes_behind_to_update.append((look_x + opp[0], look_y + opp[1], grid[look_x + opp[0]][look_y + opp[1]]))
        visited.append(box)
    
    # after everything is done, did we actually visit spots behind the other side of the box. if we did, we move the previous character, if not, it's a "."
    while len(boxes_behind_to_update) != 0:
        box = boxes_behind_to_update.pop()
        if box in visited:
            new_grid[box[0] + dir[0]][box[1] + dir[1]] = box[2]
        else:
            new_grid[box[0] + dir[0]][box[1] + dir[1]] = "."

    return new_grid

directions = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1)
}

opposite_directions = {
    "^": (1, 0),
    "v": (-1, 0),
}

box_lookaround_directions = {
    "[": (0, 1),
    "]": (0, -1)
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
    elif grid[x][y] in ["[", "]"]:
        new_grid = push(robot[0], robot[1], c, grid)
        if new_grid != False:
            grid = new_grid
            robot = [x, y]
    for r in grid:
        print(r)
    print("\n")

t = 0 
for i in range(len(grid)):
    for j in range(len(grid[i])) :
        if grid[i][j] == "[":
            t += i * 100 + j

print(t)
