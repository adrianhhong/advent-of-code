# This is my attempt at performing Dijkstra's properly.
# Importantly it:
# (1) keeps track of visited nodes, and doesn't repeat visiting those nodes visited,
# (2) Dijkstra sorts by minimum cost and chooses that next. using a heap is perfect for this.
# This uses a heap to easily sort by cost.
# heapq.heappop will grab the smallest in the heap which is 
# defaulted to the first element of a tuple https://docs.python.org/3/library/heapq.html#heapq.heapify

import heapq

lines = open("input.txt").read().split('\n')
grid = []

for l in lines:
    grid.append([int(x) for x in l])

# Utility method to check whether a point is inside the grid or not
def isInsideGrid(i, j):
	return (i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]))

# Method returns minimum cost to reach bottom right from top left
def shortest(grid):
    dir = ["u", "r", "d", "l"]
    opp_dir = ["d", "l", "u", "r"]
    # direction arrays for simplification of getting neighbour
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # (distance from (0,0), x, y, direction, dist we have travelled already in direction)
    st = [(0, 0, 0, "r", 0), (0, 0, 0, "d", 0)]
    visited = set()

    # loop for standard dijkstra's algorithm
    while (len(st)!=0):

        # get the first cell and delete it from the set
        _dis, _x, _y, _dir, dir_amount = heapq.heappop(st)
        v = (_x, _y, _dir, dir_amount)

        # if we have already visited the node we can skip it
        if v in visited:
            continue
        else:
            visited.add((_x, _y, _dir, dir_amount))

        # looping through all neighbours
        for i in range(4):
            # if we are going in the same direction and have already moved 3 spaces
            if _dir == dir[i] and dir_amount == 3:
                continue
            
            # if we are going backward
            if _dir == opp_dir[i]:
                continue

            x = _x + dx[i]
            y = _y + dy[i]

            # if not inside boundary, ignore them
            if (isInsideGrid(x, y) == 0):
                continue
            
            straight_amount = dir_amount + 1 if _dir == dir[i] else 1 
            dis = _dis + grid[x][y]
            c = (dis, x, y, dir[i], straight_amount)

            if x == len(grid) - 1 and y == len(grid[0]) - 1:
                return dis

            heapq.heappush(st, c)


print(shortest(grid))