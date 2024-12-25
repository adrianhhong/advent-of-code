input = open(0).read().splitlines()

comp_map = {}
def add_to_map(comp_map, v, k):
    if k not in comp_map:
        comp_map[k] = [v]
    else:
        comp_map[k].append(v)

for l in input:
    a, b = l.split('-')
    add_to_map(comp_map, a, b)
    add_to_map(comp_map, b, a)

def valid_connected(comp_key, connected_set):
    neighbours = comp_map[comp_key]
    for nc in neighbours:
        if nc in connected_set: continue
        if all(cs in comp_map[nc] for cs in connected_set):
            return valid_connected(nc, connected_set + [nc])
    return connected_set 

max_connected = []
for comp_key in comp_map:
    vc = valid_connected(comp_key, [])
    if len(max_connected) < len(vc):
            max_connected = vc

print(",".join(sorted(max_connected)))
