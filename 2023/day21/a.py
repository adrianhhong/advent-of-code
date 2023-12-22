from functools import cache

input = open("input.txt").read().split('\n')
grid = []

for l in input:
    grid.append(list(l))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def is_valid_position(position):
    if 0 <= position[0] < len(input) and 0 <= position[1] < len(input[0]):
        if grid[position[0]][position[1]] != "#":
            return True
    return False

@cache
def move(position, moves_left):
    if moves_left == 0:
        return [position]
    
    final_positions = []
    for n in range(4):
        new_position = (position[0] + dx[n], position[1] + dy[n])

        if is_valid_position(new_position):
            final_positions.extend(move(new_position, moves_left-1))
    
    return list(set(final_positions))


S = None
for i, row in enumerate(grid):
    for j, col in enumerate(row):
        if col == "S":
            S = (i, j)

print(len(move(S, 64)))
