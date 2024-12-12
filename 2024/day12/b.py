import copy

areas = {}
location_map = {}
input = open(0).read().split()
grid = []
og_grid = []

dir_r = [0, 1, 0, -1]
dir_c = [-1, 0, 1, 0]

for ri, r in enumerate(input):
    curr_r = list(r)
    grid.append(curr_r)
    og_grid = copy.deepcopy(grid)

def in_grid(r, c):
    if 0<=r<len(grid) and 0<= c<len(grid[0]):
        return True
    return False


def bfs(r,c,grid):
    q = [(r,c)]
    areas[(r,c)] = 1
    location_map[(r,c)] = [(r,c)]
    letter = grid[r][c]
    grid[r][c] = "0"
    while (len(q) > 0):
        curr_r, curr_c = q.pop(0)
        for i in range(4):
            r2 = curr_r + dir_r[i]
            c2 = curr_c + dir_c[i]
            if not in_grid(r2,c2) or grid[r2][c2] == "0" or grid[r2][c2] != letter: 
                continue
            grid[r2][c2] = "0"
            q.append((r2,c2))
            areas[(r,c)] += 1
            location_map[(r,c)].append((r2,c2))

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "0":
            continue
        else:
            bfs(i,j,grid)

corners = {} # {(0,0):  (0,0,2)} <- (pos looking SE, numb corners)
# 
#               pos of one of the letters in that shape

# in a rectangle, there are the same amount of corners as sides

# get a location. check the 2 directions and that diagonal. e.g N, NE, E. If it has:
# 0 parts = corner 
#           x
# 1 part next to it = not a corner
#           x x
# 1 part diagonal = 2 corners
#           x
#             x
# 2 parts = corner
#           x x
#           x
# 3 parts = not a corner
#           x x
#           x x
# Save the direction checked. If equivalent was checked, don't check twice.
# e.g. (0,0) SE  == (0,1) SW == (1,0) NE == (1,1) NW

def convert_corner_to_SE_equivalent(position, corner_direction):
    if corner_direction == "SE":
        return position
    if corner_direction == "SW": # if im looking SW at a corner, it's as if i am one to the left, looking SE
        return (position[0], position[1]-1)
    if corner_direction == "NE":
        return (position[0]-1, position[1])
    if corner_direction == "NW":
        return (position[0]-1, position[1]-1)

# we know that if the distance going up down left or right is 2, it is in the diagonal
def is_diagonally_across(p1, p2):
    return abs(p1[0] - p2[0])+abs(p1[1] - p2[1]) == 2

t = 0

diag_dir = {
    "SE": [(0,1), (1,0), (1,1)],
    "SW": [(0,-1), (1,0), (1,-1)],
    "NE": [(-1,0), (0,1), (-1,1)],
    "NW": [(-1,0), (0,-1), (-1,-1)]
}

for position, locations in location_map.items():
    letter = og_grid[position[0]][position[1]]
    for loc in locations:
        for diag, vals in diag_dir.items():
            dirs_that_have_letter = []
            
            for dirs in vals:
                r2 = loc[0] + dirs[0]
                c2 = loc[1] + dirs[1]
                if in_grid(r2,c2) and (r2,c2) in locations:
                    dirs_that_have_letter.append((r2,c2))
            if len(dirs_that_have_letter) == 3:
                continue
            SE_equivalent = convert_corner_to_SE_equivalent(loc, diag)

            if len(dirs_that_have_letter) == 1 and is_diagonally_across(loc, dirs_that_have_letter[0]):
                if position in corners:
                    corners[position].add((SE_equivalent[0], SE_equivalent[1], 2))
                else:
                    corners[position] = {(SE_equivalent[0], SE_equivalent[1], 2)}
            if len(dirs_that_have_letter) == 0 or len(dirs_that_have_letter) == 2:
                if position in corners:
                    corners[position].add((SE_equivalent[0], SE_equivalent[1], 1))
                else:
                    corners[position] = {(SE_equivalent[0], SE_equivalent[1], 1)}
        

print(location_map)
print(areas)
print(corners)

for position, a in areas.items():
    ct = 0
    for c in corners[position]:
        ct += c[2]
    print(ct)
    t += a*ct
print(t)
