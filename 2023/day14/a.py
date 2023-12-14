grid = open("input.txt").read().split('\n')

# rotate anticlockwise 90 degrees. Top row was previously right column.
def rotate_matrix( m ):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]

rotated_grid = rotate_matrix(grid)

# calculate if gravity falls to the left
for row in rotated_grid:
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

total = 0

# 0 -> 10, 1-> 9, 2 -> 8
for row in rotated_grid:
    for i, c in enumerate(row):
        if c in 'O':
            total += len(rotated_grid) - i


print(total)