from toposort import toposort

first, second = open(0).read().split('\n\n')

start_map = {}
print(first)

for f in first.splitlines():
    wire, val = f.split(": ")
    start_map[wire] = bool(int(val))

dependency = {}

gates = {}

for s in second.splitlines():
    a, b = s.split('->')
    x, gate, y = a.split()
    dependency[b.strip()] = {x, y}
    gates[b.strip()] = ((x, y), gate)


def bool_calc(a, b, comp):
    if comp == "AND":
        return int(bool(a) & bool(b))
    if comp == "OR":
        return int(bool(a) | bool(b))
    if comp == "XOR":
        return int(bool(a) ^ bool(b))

sort = list(toposort(dependency))

for s in sort:
    for d in s:
        if d not in start_map:
            # calc
            vals, gate = gates[d]
            print(d, vals, gate)
            start_map[d] = bool_calc(start_map[vals[0]], start_map[vals[1]], gate)
            print(start_map[d])

z = ""

print(sorted(start_map.items()))

for k,v in reversed(sorted(start_map.items())):
    if k.startswith('z'):
        z += str(int(v))

print(z)
print(int(z, 2))