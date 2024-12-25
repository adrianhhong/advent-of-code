import collections

grid = []

for l in open(0).read().splitlines():
    grid.append(list(l))

start = []
end = []

cheat_candidates = []

distance_grid = [[-1] * len(grid) for _ in range(len(grid))]

def in_bounds(x, y):
    return 0 < x < len(grid) - 1 and 0 < y < len(grid[0]) - 1

for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == "S":
            start = (r, c)
        if grid[r][c] == "E":
            end = (r, c)

norm_time = 0

def get_distance_grid(grid, start):
    queue = collections.deque([[start]])
    seen = set([start])
    distance_grid[start[0]][start[1]] = 0
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        global norm_time
        if x == end[0] and y == end[1] and norm_time == 0:
            norm_time = len(path) - 1 # -1 for starting position
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if in_bounds(x2, y2) and grid[x2][y2] != "#" and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))
                distance_grid[x2][y2] = len(path)
    return seen

possible_start_locations = get_distance_grid(grid, start)

def get_locations_within_radius(grid, start, radius):
    seen = set([])
    for dx in range(-radius, radius+1):
        for dy in range(-radius + abs(dx), radius+1 - abs(dx)):
            x2 = start[0] + dx
            y2 = start[1] + dy
            if in_bounds(x2, y2) and grid[x2][y2] != "#" and (x2, y2) not in seen:
                seen.add((x2, y2, abs(dx)+abs(dy)))
    non_wall_seen = set([])
    for s in seen:
        if grid[s[0]][s[1]] != "#":
            non_wall_seen.add(s)
    return non_wall_seen


t = 0

for p in possible_start_locations:
    loc_in_radius = get_locations_within_radius(grid, p, 20)
    for l in loc_in_radius:
        d_to_start_loc = distance_grid[p[0]][p[1]]
        d_cheat = l[2]
        d_to_end = norm_time - distance_grid[l[0]][l[1]]
        distance = d_to_start_loc + d_cheat + d_to_end

        if (norm_time - distance) >= 100:
            t += 1

print(t)
