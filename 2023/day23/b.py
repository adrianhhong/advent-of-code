import sys
sys.setrecursionlimit(1000000)

input = open("input.txt").read().split('\n')
grid = []
start = []
end = ()
graph = {}

for i, l in enumerate(input):
    if i == 0:
        start_y = l.index(".")
        start = (0, start_y)
    if i == len(input) - 1:
        end_y = l.index(".")
        end = (len(input) - 1, end_y)
    grid.append(list(l))

def is_valid(next_position):
    if next_position[0] < 0 or next_position[0] >= len(input) or next_position[1] < 0 or next_position[1] >= len(input[0]):
        return False
    if grid[next_position[0]][next_position[1]] == "#":
        return False
    return True

# Convert the grid to a graph so that we can collapse long straight paths down
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y] == "#":
            continue

        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        for i in range(4):
            adjx = x + dx[i]
            adjy = y + dy[i]

            if is_valid((adjx, adjy)):
                if (x,y) in graph:
                    graph[(x,y)].append((adjx, adjy))
                else:
                    graph[(x,y)] = [(adjx, adjy)]

# Any paths that have 2 neighbours can be collapsed down
# This now stores it as (count, (next_node))
def get_new_edge(graph, start, end):
    count = 1
    while len(graph[end]) == 2:
        count += 1
        next = ()
        for n in graph[end]:
            if n != start:
                next = n
        start, end = (end, next)
    
    return (count, end)

def collapse_single_paths(graph):
    new_graph = {}
    for k, v in graph.items():
        if len(v) != 2:
            new_graph[k] = [get_new_edge(graph, k, n) for n in v]
    return new_graph

distances = []

def get_paths(graph, current_edges, path, running_count):

    for e in current_edges:
        count, position = e

        # if we reach the end
        if position == end:
            distances.append(running_count + count)
            continue

        # if we haven't gone down this path before
        if position not in path:
            path.append(position)
            get_paths(graph, graph[position], path, running_count+count)
            path.pop(-1)

collapsed_graph = collapse_single_paths(graph)
get_paths(collapsed_graph, collapsed_graph[start], [start], 0)
print(distances)
print(max(distances))