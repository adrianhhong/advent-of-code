import collections
import copy

grid = []

for l in open(0).read().splitlines():
    grid.append(list(l))

start = []
end = []

cheat_candidates = []

def in_bounds(x, y):
    return 0 < x < len(grid) - 1 and 0 < y < len(grid[0]) - 1

def cheatable(x, y):
    return (grid[x+1][y] == "#" + grid[x-1][y] == "#" + grid[x][y+1] == "#" + grid[x][y-1]) <= 2

for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == "S":
            start = (r, c)
        if grid[r][c] == "E":
            end = (r, c)
        if grid[r][c] == "#" and in_bounds(r, c) and cheatable(r, c):
            cheat_candidates.append((r,c))


def bfs(grid, start):
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if x == end[0] and y == end[1]:
            return len(path) - 1 # -1 for starting position
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if in_bounds(x2, y2) and grid[x2][y2] != "#" and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))

norm_time = bfs(grid, start)

print(norm_time)

t = 0


for c in cheat_candidates:
    grid_cheat = copy.deepcopy(grid)
    grid_cheat[c[0]][c[1]] = "."
    cheat_time = bfs(grid_cheat, start)
    if norm_time - cheat_time >= 100:
        t += 1
        print(cheat_time)

print(t)

# took like 10 min lol