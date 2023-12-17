# This is a cleaned up version of how I solved it.

# This doesn't actually implement Dijkstra's algo
# This will iterate through every path and find min
# Whilst it will find the answer, it takes a long time
# The reason this isn't Dijkstra's is that:
# (1) Dijkstra keeps track of visited nodes, and doesn't repeat visiting
# those nodes visited,
# (2) Dijkstra sorts by minimum cost and chooses that next. using a 
# heap is perfect for this.

lines = open("input.txt").read().split('\n')
grid = []

for l in lines:
    grid.append([int(x) for x in l])


# Utility method to check whether a point is inside the grid or not
def isInsideGrid(i, j):
	return (i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]))

def getMinBottomRight(seen, grid):
    all_dis = []
    for c, dis in seen.items():
        if c[0] == len(grid) - 1 and c[1] == len(grid[0]) - 1 and c[3] >=4: # must travel at least 4 before reaching the end
            all_dis.append(dis)
    return min(all_dis)

# Method returns minimum cost to reach bottom right from top left
def shortest(grid):
    dir = ["u", "r", "d", "l"]
    opp_dir = ["d", "l", "u", "r"]
    # direction arrays for simplification of getting neighbour
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    st = []

    # insert (0, 0) going right
    st = [(0, 0, "r", 0)]
    seen = {(0, 0, "r", 0): 0}

    # loop for standard dijkstra's algorithm
    while (len(st)!=0):
        
        # get the first cell and delete it from the set
        k = st[0]
        st = st[1:]

        # looping through all neighbours
        for i in range(4):
            # if we are going in the same direction and have already moved 10 spaces
            if k[2] == dir[i] and k[3] == 10:
                continue

            # if we are going in a different direction and haven't moved 4 spaces yet
            if k[2] != dir[i] and k[3] < 4:
                continue

            # if we are going backward
            if k[2] == opp_dir[i]:
                continue

            x = k[0] + dx[i]
            y = k[1] + dy[i]


            # if not inside boundary, ignore them
            if (isInsideGrid(x, y) == 0):
                continue

            straight_amount = k[3] + 1 if k[2] == dir[i] else 1 
            c = (x, y, dir[i], straight_amount)
            dis = seen[k] + grid[x][y]

            if c not in seen:
                st.append(c)
                seen[c] = dis
            else:
                if dis < seen[c]:
                    st.append(c)
                    seen[c] = dis

    return getMinBottomRight(seen, grid)


print(shortest(grid))