import collections 

grid = [list(l) for l in open(0).read().splitlines()]

print(grid)

start = []
end = []

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "S":
            start = (i, j)
        if grid[i][j] == "E":
            end = (i, j)

directions = {
    "N": (-1, 0),
    "E": (0, 1),
    "S": (1, 0),
    "W": (0, -1)
}

def bfs(grid, start, end):
    queue = collections.deque([(start[0], start[1], "E", 0)])
    seen = set([(start[0], start[1], "E")])
    min_seen_map = {(start[0], start[1], "E"): 0}
    while queue:
        path = queue.popleft()
        x, y, dir, cost = path
        x2 = x + directions[dir][0]
        y2 = y + directions[dir][1]
        if grid[x2][y2] != "#":
            new_cost = cost + 1
            if (x2, y2, dir) not in seen:
                queue.append((x2, y2, dir, new_cost))
                seen.add((x2, y2, dir))
                min_seen_map[((x2, y2, dir))] = new_cost
            else:
                if min_seen_map[(x2, y2, dir)] > new_cost:
                    queue.append((x2, y2, dir, new_cost))
                    min_seen_map[((x2, y2, dir))] = new_cost
        remaining_dir = ["N", "E", "S", "W"]
        remaining_dir.remove(dir)
        for d in remaining_dir:
            new_cost = cost + 1000
            if (x, y, d) not in seen:
                queue.append((x, y, d, new_cost))
                seen.add((x, y, d))
                min_seen_map[((x, y, d))] = new_cost
            else:
                if min_seen_map[(x, y, d)] > new_cost:
                    queue.append((x, y, d, new_cost))
                    min_seen_map[((x, y, d))] = new_cost

    
    print(min_seen_map)

    min = float("inf")
    print(end)
    for r in seen:
        if (r[0], r[1]) == end:
            for d in ["N", "E", "S", "W"]:
                if min_seen_map[(r[0], r[1], d)] < min:
                    min = min_seen_map[(r[0], r[1], d)]
    return min

min = bfs(grid, start, end)
print(min)