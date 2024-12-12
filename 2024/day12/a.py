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

perimeters = {}
t = 0

for position, locations in location_map.items():
    letter = og_grid[position[0]][position[1]]
    for loc in locations:
        for i in range(4):
            r2 = loc[0] + dir_r[i]
            c2 = loc[1] + dir_c[i]
            if not in_grid(r2,c2) or og_grid[r2][c2] is not letter:
                if position in perimeters:
                    perimeters[position] += 1
                else:
                    perimeters[position] = 1

print(location_map)
print(areas)
print(perimeters)

for position, a in areas.items():
    t+= a * perimeters[position]

print(t)
