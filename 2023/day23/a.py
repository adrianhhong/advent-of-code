import sys
sys.setrecursionlimit(1000000)

input = open("input.txt").read().split('\n')
grid = []
start = []
end = ()

for i, l in enumerate(input):
    if i == 0:
        start_y = l.index(".")
        start = (0, start_y)
    if i == len(input) - 1:
        end_y = l.index(".")
        end = (len(input) - 1, end_y)
    grid.append(list(l))

def is_valid(next_position, prev_position, path):
    if next_position[0] < 0 or next_position[0] >= len(input) or next_position[1] < 0 or next_position[1] >= len(input[0]):
        return False
    if grid[next_position[0]][next_position[1]] == "#":
        return False
    if next_position in path:
        return False
    if grid[next_position[0]][next_position[1]] == ">" and prev_position[1] - next_position[1] == 1: # we are going left
        return False
    if grid[next_position[0]][next_position[1]] == "v" and prev_position[0] - next_position[0] == 1: # we are going up
        return False
    return True

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

distances = []

# DFS using recursion
def get_paths(position, path):
    x, y = position

    if x == end[0] and y == end[1]:
        distances.append(len(path))
        return

    for i in range(4):
        adjx = x + dx[i]
        adjy = y + dy[i]

        if not is_valid((adjx, adjy), position, path):
            continue

        path.append((adjx, adjy))
        get_paths((adjx, adjy), path)
        path.pop(-1)

get_paths(start, [])
print(max(distances))