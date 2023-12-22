input = open("input.txt").read().split('\n')
grid = []

for l in input:
    grid.append(list(l))

direction_array = ["U", "R", "D", "L"]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def is_valid_position(position):
    if 0 <= position[0] < len(input) and 0 <= position[1] < len(input[0]):
        if grid[position[0]][position[1]] != "#":
            return True
    return False
        

# cache was taking ages.. use BFS instead
def bfs(position):
    visited = set()
    queue = []
    final_positions = set()

    x, y, moves_left = position
    visited.add((x, y))
    queue.append([x, y, moves_left])

    while queue:
        p = queue.pop(0)

        if p[2] % 2 == 0:
            final_positions.add((p[0], p[1]))
        if p[2] == 0:
            continue

        for n in range(4):
            new_position = (p[0] + dx[n], p[1] + dy[n])
            if not is_valid_position(new_position):
                continue
            if new_position not in visited:
                visited.add(new_position)
                queue.append([new_position[0], new_position[1], p[2] - 1])
    
    return len(final_positions)


# S is in the middle
S = None
for i, row in enumerate(grid):
    for j, col in enumerate(row):
        if col == "S":
            S = (i, j)

width = len(grid[0])
height = len(grid)

# Assume it's a square
assert width == height
steps = 26501365 
# The furthest we can go is to the very edge of one grid very far away
assert S[0] == steps % width
extended_width = steps // width - 1


total = 0
# In the middle grid we can only land on even squares if our steps is an odd number
# All diagonals of this middle grid we can only land on even squares
# just choose a step size where we know we will visit every point
# width * 2 is plenty big enough. We also need to start on odd square which is why +1
total += (extended_width // 2 * 2 + 1) ** 2 * bfs([S[0], S[1], width*2 + 1])

# In the grids adjacent to the middle grid, and all diagonals of that,
# we can only land on odd squares
# just choose a step size where we know we will visit every point
# width * 2 is plenty big enough. We have to start on even square.
total += ((extended_width + 1) // 2 * 2) ** 2 * bfs([S[0], S[1], width*2])

# the very top grid. we start at the bottom middle
total += bfs([height - 1, width // 2, height -1])
# the very right grid. we start at the left middle
total += bfs([height // 2, 0, width-1])
# very left grid.
total += bfs([height // 2, width - 1, width-1])
# very bottom grid
total += bfs([0, width // 2, height-1])

# the small triangle of the top right. we have width//2-1 steps to go when we reach that bottom left corner
small_tr = bfs([height - 1, 0, width // 2 - 1])
small_br = bfs([0, 0, width // 2 - 1])
small_bl = bfs([0, width-1, width // 2 - 1])
small_tl = bfs([height - 1, width -1, width // 2 - 1])
# we observe each extended_width + 1 times
total += (extended_width + 1) * (small_tr + small_br + small_bl + small_tl)

# the small triangle of the top right. we reach these a whole width before small, so need to add a width to each starting steps
large_tr = bfs([height - 1, 0, width * 3// 2 - 1])
large_br = bfs([0, 0, width * 3// 2 - 1])
large_bl = bfs([0, width-1, width * 3// 2 - 1])
large_tl = bfs([height - 1, width -1, width *3// 2 - 1])
# we observe each e times
total += extended_width * (large_tr + large_br + large_bl + large_tl)

print(total)