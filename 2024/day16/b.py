import collections 

grid = [list(l) for l in open(0).read().splitlines()]

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

# from all seen, find the states that give us the minimum to reach the end
def find_end_states(seen, min_seen_map):
    end_states = set()
    min = float("Inf")
    for r in seen:
        if (r[0], r[1]) == end:
            if min_seen_map[r] < min:
                min = min_seen_map[r]
                end_states = set()
                end_states.add(r)
            elif min_seen_map[r] == min:
                end_states.add(r)
    return end_states

def get_all_ways_to_reach_end_states(end_states, backtrack):
    states = collections.deque(end_states)
    seen_fill = set(end_states)
    while states:
        key = states.popleft()
        previous_state = backtrack.get(key, [])
        for ps in previous_state:
            if ps is None: continue
            states.append(ps)
            seen_fill.add(ps)
    seen_fill_no_dir = set()
    for s in seen_fill:
        seen_fill_no_dir.add((s[0], s[1]))
    return seen_fill_no_dir

def bfs(grid, start):
    queue = collections.deque([(start[0], start[1], "E", 0)])
    seen = set([(start[0], start[1], "E")])
    min_seen_map = {(start[0], start[1], "E"): 0}
    backtrack = {(start[0], start[1], "E"): (None, None, None)} # best way to get to a key is the value
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
                backtrack[(x2, y2, dir)] = set([(x, y, dir)])
            else:
                if min_seen_map[(x2, y2, dir)] > new_cost:
                    queue.append((x2, y2, dir, new_cost))
                    min_seen_map[((x2, y2, dir))] = new_cost
                    backtrack[(x2, y2, dir)] = set([(x, y, dir)])
                elif min_seen_map[(x2, y2, dir)] == new_cost:
                    backtrack[(x2, y2, dir)].add((x, y, dir))
        remaining_dir = ["N", "E", "S", "W"]
        remaining_dir.remove(dir)
        for d in remaining_dir:
            new_cost = cost + 1000
            if (x, y, d) not in seen:
                queue.append((x, y, d, new_cost))
                seen.add((x, y, d))
                min_seen_map[((x, y, d))] = new_cost
                backtrack[(x, y, d)] = set([(x, y, dir)])
            else:
                if min_seen_map[(x, y, d)] > new_cost:
                    queue.append((x, y, d, new_cost))
                    min_seen_map[((x, y, d))] = new_cost
                    backtrack[(x, y, d)] = set([(x, y, dir)])
                elif min_seen_map[(x, y, d)] == new_cost:
                    backtrack[(x, y, d)].add((x, y, dir))


    end_states = find_end_states(seen, min_seen_map)
    print(len(get_all_ways_to_reach_end_states(end_states, backtrack)))


bfs(grid, start)