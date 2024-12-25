import collections

input = open(0).read().splitlines()

comp_map = {}
def add_to_map(comp_map, v, k):
    if k not in comp_map:
        comp_map[k] = [v]
    else:
        comp_map[k].append(v)


for l in input:
    a, b = l.split('-')
    add_to_map(comp_map, a, b)
    add_to_map(comp_map, b, a)


#bfs
def get_cycles(start, comp_map):
    queue = collections.deque([[(start, 0)]])
    # seen = set([start])
    paths = []
    while queue:
        path = queue.popleft()
        computer, depth = path[-1]
        if depth > 3:
            continue
        if computer == start and depth == 3:
            ps = list(map(lambda p: p[0], path[:-1]))
            paths.append(ps)
            continue
        for nc in comp_map[computer]:
            # if nc not in seen:
                queue.append(path + [(nc, depth + 1)])
                # seen.add(nc)
    return paths

def starts_with_t(cycle):
    for c in cycle:
        if c.startswith("t"):
            return True
    return False

t = 0
cycles = []
for k in comp_map:
    cycles += get_cycles(k, comp_map)
cycles_remove_dupe = set(tuple(sorted(l)) for l in cycles)
for c in cycles_remove_dupe:
    if starts_with_t(c):
        t += 1

print(t)
