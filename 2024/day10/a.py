grid = []
th = []

input = open(0).read().splitlines()

for ri, r in enumerate(input):
    curr_r = list(map(int, list(r)))
    grid.append(curr_r)
    for ci, c in enumerate(curr_r):
        if c == 0:
            th.append((ri, ci))

print(grid)
print(th)

dir_r = [0, 1, 0, -1]
dir_c = [-1, 0, 1, 0]
visited = []

def in_grid(r, c):
    if 0<=r<len(grid) and 0<= c<len(grid[0]):
        return True
    return False

visited = []
def dfs(r,c,h): 
    for i in range(4):
        r2 = r + dir_r[i]
        c2 = c + dir_c[i]
        if in_grid(r2,c2) and (r2,c2,h+1) not in visited and grid[r2][c2] == h+1:
            visited.append((r2,c2,h+1))
            dfs(r2,c2,h+1)
t=0
for ths in th:
    visited = []
    dfs(ths[0],ths[1], 0)
    st = 0
    for v in visited:
        if v[2] == 9:
            st+=1
    t += st
    print(st)

print(t)

