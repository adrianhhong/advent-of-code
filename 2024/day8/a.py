input = open(0).read().splitlines()

antenna_map = {}

for ri, r in enumerate(input):
    for ci, c in enumerate(r):
        if c == ".":
            continue
        if c in antenna_map:
            antenna_map[c].append((ri,ci))
        else:
            antenna_map[c] = [(ri,ci)]

antenna_list = list(map(lambda x: x[1], antenna_map.items()))

def in_grid(an):
    if 0 <= an.real < len(input) and 0 <= an.imag < len(input[0]):
        return True
    return False

antinode_set = set()

for al in antenna_list:
    for i in range(0,len(al)-1):
        for j in range((i+1),len(al)):
            a = complex(al[i][0], al[i][1])
            b = complex(al[j][0], al[j][1])
            offset = a-b
            an_a = a+offset
            an_b = b-offset
            if in_grid(an_a):
                antinode_set.add(an_a)
            if in_grid(an_b):
                antinode_set.add(an_b)

print(len(antinode_set))
