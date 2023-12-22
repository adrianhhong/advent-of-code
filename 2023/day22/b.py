import copy

input = open("input.txt").read().split('\n')

blocks = []

for n, l in enumerate(input):
    start, end = l.split("~")
    start = list(map(int, start.split(",")))
    end = list(map(int, end.split(",")))
    blocks.append([start, end, n])

# sort by lowest blocks because those fall first
blocks = sorted(blocks, key = lambda x: int(x[0][2]))

fallen_blocks = []
# [block supporting, block being supported] 
landed_mappings = []

for b in blocks:
    bsx, bsy, bsz = b[0]
    bex, bey, bez = b[1]
    has_landed_on_block = False
    just_added_z = False # this will help us check what else the landed block sits on

    for f in fallen_blocks:
        fsx, fsy, fsz = f[0]
        fex, fey, fez = f[1]
        
        is_x_overlapping = bex >= fsx and fex >= bsx
        is_y_overlapping = bey >= fsy and fey >= bsy
        if is_x_overlapping and is_y_overlapping and not just_added_z:
            # it will land on this fallen block
            fallen_blocks.append([[bsx, bsy, fez+1], [bex, bey, (bez-bsz)+(fez+1)], b[2]])
            landed_mappings.append([f[2], b[2]])
            has_landed_on_block = True
            just_added_z = fez
        elif just_added_z:
            if is_x_overlapping and is_y_overlapping and just_added_z == fez:
                landed_mappings.append([f[2], b[2]])


    if not has_landed_on_block: # i.e. it falls to the ground
        fallen_blocks.append([[bsx, bsy, 1], [bex, bey, bez-bsz+1], b[2]])

    # after adding the block to fallen sort by highest block since blocks will land on those first
    fallen_blocks = sorted(fallen_blocks, key = lambda x: int(x[1][2]), reverse=True)

# supporting map is a map where the key is the block being supported, and the values are the blocks that are supporting that block
supporting_map = {}
for m in landed_mappings:
    if m[1] in supporting_map:
        supporting_map[m[1]].append(m[0]) 
    else:
        supporting_map[m[1]] = [m[0]]

cant_disintegrate = set()

# much better way to solve it than i did for part a..
for v in supporting_map.values():
    if len(v) == 1:
        cant_disintegrate.add(v[0])

total = 0

# Test for every block we said we could not disintegrate.
# The idea is that we remove that block as a support
# We go through every other block. Was this removed block the only one supporting some other block?
# If so, we remove those blocks too and add 1 for each to the total
# When we reach a point where blocks were being supported by more than just that 1 block, which is where we end the while loop
for cd in cant_disintegrate:
    supporting_map2 = copy.deepcopy(supporting_map)
    disintegrate = [cd]

    while(1):
        # get rid of all we want to disintegrate in supporting_map2
        for d in disintegrate:
            for v in supporting_map2.values():
                if d in v: # we found a supporting block we can try disintegrating
                    v.pop(v.index(d))
        
        # reset disintegrate
        disintegrate = []

        # if a block is not critical, then there was another block also supporting a block 
        all_not_critical = True

        # check if any vals are empty now
        for k, m in supporting_map2.items():
            if len(m) == 0:
                all_not_critical = False
                disintegrate.append(k)
                total += 1

        for d in disintegrate:
            del supporting_map2[d]
        
        if all_not_critical:
            break

print(total)
