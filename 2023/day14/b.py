grid = open("input.txt").read().split('\n')

# rotate anticlockwise 90 degrees. Top row was previously right column.
def rotate_matrix_anti( m ):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]

# rotate clockwise 90 degrees. Top row becomes right column.
def rotate_matrix_clock(m):
    return [list(reversed(col)) for col in zip(*m)]

# Rotate anti clockwise cause it's easier to calculate where the rocks fall if it's the left since
# all we need to look at is the string
rotated_grid = rotate_matrix_anti(grid)

# We create a hash of all the EAST grids we have seen. 
grid_hash = {}

# times is the FURTHER amount of times we need to rotate to get to the end state
times = 0

# Instead of tilting things N, S, E, W. I rotate the grid so that the tilt direction is to the left, and enact gravity to the left.
def left_gravity(grid):
    for row in grid:
        # we want all the rocks to move left
        space_to_move = 0
        for k, c in enumerate(row):
            if c in '.':
                space_to_move += 1
            elif c in '#':
                space_to_move = 0
            elif c in 'O' and space_to_move != 0:
                row[k-space_to_move] = 'O'
                row[k] = '.'
    return grid

# n is 0, w is 1, s is 2, e is 3
for r in range(1000000000*4):
    # The first r is already in the correct position
    if r != 0:
        rotated_grid = rotate_matrix_clock(rotated_grid)

    rotated_grid = left_gravity(rotated_grid)
    
    # When we have gone through 1 cycle and we have reached EAST
    if r % 4 == 3:
        # tuples are hashable so we change it to a tuple of tuples
        current_hash = tuple(tuple(x) for x in rotated_grid)
        if current_hash in grid_hash:
            diff = r - grid_hash[current_hash] # diff is the number of rotations before we are repeating again
            times = (1000000000*4 - 1 - r) % diff # if this keeps repeating, how many more rotations do we need to 1trill cycles
            break
        grid_hash[current_hash] = r

# now we have the times needed to get to 1trill cycles, we perform that
for i in range(times):
    rotated_grid = left_gravity(rotate_matrix_clock(rotated_grid))

# since it will end with EAST to the left, we need to rotate 180 degrees to get NORTH back to the top
right_way_grid = rotate_matrix_anti(rotate_matrix_anti(rotated_grid))

total = 0

for i, row in enumerate(right_way_grid):
    for c in row:
        if c in 'O':
            total += len(row) - i

print(total)