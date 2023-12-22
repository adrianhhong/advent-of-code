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
        
for i in fallen_blocks:
    print(i)

print(landed_mappings)

cant_disintegrate = set()

for n in range(len(blocks)): # for every block
    num_supporting = 0
    found_one = -1
    for m in landed_mappings:
        if m[1] == n:
            num_supporting += 1
            found_one = m[0]
        if num_supporting == 2:
            found_one = -1
            break

    if found_one != -1:
        cant_disintegrate.add(found_one)

print(len(blocks) - len(cant_disintegrate))

