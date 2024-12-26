import itertools


all = open(0).read().split('\n\n')

def get_lock(grid):
    lock = [None] * len(grid[0])
    for r in range(1, len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == "." and lock[c] == None:
                lock[c] = r-1
    return lock

def get_key(grid):
    key = [None] * len(grid[0])
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == "#" and key[c] == None:
                key[c] = len(grid) - r - 1
    return key

def is_lock(first_row):
    for c in first_row:
        if c == "#":
            return True

locks = []
keys = []
for a in all:
    grid = []
    for l in a.splitlines():
        grid.append(list(l))
    if is_lock(grid[0]):
        locks.append(get_lock(grid))
    else:
        keys.append(get_key(grid))

def valid_combo(l,k):
    for i in range(len(l)):
        if l[i] + k[i] > 5:
            return False
    return True

t= 0
for l, k in itertools.product(locks, keys):
    if valid_combo(l,k):
        t += 1

print(t)