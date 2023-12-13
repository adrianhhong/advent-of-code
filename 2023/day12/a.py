grid = []
broken_groups = []

lines = open("input.txt").read().split('\n')
for l in lines:
    (g, b) = l.split(' ')
    grid.append(list(g))
    broken_groups.append(list(map(int, b.split(','))))

# print(grid)
# print(broken_groups)

from itertools import product

def filler(word, from_char, to_char):
    options = [(c,) if c != from_char else (from_char, to_char) for c in word]
    return (''.join(o) for o in product(*options))

num_perms_matching = 0

for i, l in enumerate(grid):
    all_perms = list(filler(l, "?", "#"))
    for p in all_perms:
        curr_group = []
        count = 0
        for c in p:
            if c in "?.":
                if count > 0:
                    curr_group.append(count)
                    count = 0
            else:
                count += 1
        if count > 0:
            curr_group.append(count)
            count = 0
        # print(curr_group, count)
        # print(p, curr_group)
        if (curr_group==broken_groups[i]):
            num_perms_matching += 1


print(num_perms_matching)
                
