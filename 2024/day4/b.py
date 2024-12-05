import re

input = open(0).read().splitlines()

grid = []

for row in input:
    grid.append(list(row))

t=0

tl = [(-1,-1), (1,1)]
bl = [(1,-1), (-1,1)]

for ri, r in enumerate(grid):
    for ci, c in enumerate(r):
        # directions = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]
        if grid[ri][ci] == 'A':
            print(ri, ci)
            in_bounds = (ri-1 >= 0) and (ri+1 < len(grid)) and (ci-1 >= 0) and (ci+1 < len(grid[0]))
            if in_bounds:
                tl_is_M = (grid[ri+tl[0][0]][ci+tl[0][1]] == 'M') and (grid[ri+tl[1][0]][ci+tl[1][1]] == 'S')
                tl_is_S = (grid[ri+tl[0][0]][ci+tl[0][1]] == 'S') and (grid[ri+tl[1][0]][ci+tl[1][1]] == 'M')
                bl_is_M = (grid[ri+bl[0][0]][ci+bl[0][1]] == 'M') and (grid[ri+bl[1][0]][ci+bl[1][1]] == 'S')
                bl_is_S = (grid[ri+bl[0][0]][ci+bl[0][1]] == 'S') and (grid[ri+bl[1][0]][ci+bl[1][1]] == 'M')
                print(tl_is_M, tl_is_S, bl_is_M, bl_is_S)

                if (tl_is_M or tl_is_S) and (bl_is_M or bl_is_S):
                    t += 1

        # for i, char in enumerate('XMAS'):
        #     remove_d = []
        #     print(len(directions))
        #     for d in directions:
        #         # print(directions)
        #         print(char, d, ri, ci)
        #         if (ri+(i*d[0]) >= 0) and (ri+(i*d[0]) < len(grid)) and (ci+(i*d[1]) >= 0) and (ci+(i*d[1]) < len(grid[0])) and (grid[ri+(i*d[0])][ci+(i*d[1])] == char):
        #             if (i == 3):
        #                 t += 1
        #                 print('found', ri+(i*d[0]), ci+(i*d[1]))
        #             print('good')
        #         else:
        #             remove_d.append(d)
        #             # break
        #     for d in remove_d:
        #         directions.remove(d)


print(t)
