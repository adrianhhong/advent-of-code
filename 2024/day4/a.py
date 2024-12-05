import re

input = open(0).read().splitlines()

grid = []

for row in input:
    grid.append(list(row))

t=0

for ri, r in enumerate(grid):
    for ci, c in enumerate(r):
        directions = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]
        for i, char in enumerate('XMAS'):
            remove_d = []
            print(len(directions))
            for d in directions:
                # print(directions)
                print(char, d, ri, ci)
                if (ri+(i*d[0]) >= 0) and (ri+(i*d[0]) < len(grid)) and (ci+(i*d[1]) >= 0) and (ci+(i*d[1]) < len(grid[0])) and (grid[ri+(i*d[0])][ci+(i*d[1])] == char):
                    if (i == 3):
                        t += 1
                        print('found', ri+(i*d[0]), ci+(i*d[1]))
                    print('good')
                else:
                    remove_d.append(d)
                    # break
            for d in remove_d:
                directions.remove(d)


print(t)
