import collections
import copy

input = open(0).read().splitlines()
size = 71
# size = 7
bytes_fallen = 1024
# bytes_fallen = 12

og_grid = [["."] * size for i in range(size)]

def bfs(grid, start):
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if x == size-1 and y == size-1:
            return path
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < size and 0 <= y2 < size and grid[x2][y2] != "#" and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))


for i in range(bytes_fallen, len(input)):
    grid = copy.deepcopy(og_grid)

    for j in range(i):
        l = input[j]
        c, r = list(map(int, l.split(',')))
        grid[r][c] = "#"
    
    if bfs(grid, (0,0)) ==  None:
        print(input[i-1])
        break

