import collections

input = open(0).read().splitlines()
size = 71
grid = [["."] * size for i in range(size)]

print(grid)

for i in range(1024):
    l = input[i]
    c, r = list(map(int, l.split(',')))
    grid[r][c] = "#"

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

print(bfs(grid, (0,0)))
print(len(bfs(grid, (0,0))) -1)

