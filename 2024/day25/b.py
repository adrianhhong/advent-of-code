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

x = ""
y = ""
z = ""

print(sorted(start_map.items()))

for k,v in reversed(sorted(start_map.items())):
    if k.startswith('z'):
        z += str(int(v))
    if k.startswith('y'):
        y += str(int(v)) 
    if k.startswith('x'):
        x += str(int(v))   



print("0b " + x)
print(int(x, 2))
print("0b " + y)
print(int(y, 2))
print("0b" + z)
print(bin(int(x, 2) + int(y, 2)))
print(int(z, 2))
binary_diff = bin(int(z,2) ^ (int(x, 2) + int(y, 2)))
print("   " + binary_diff)
print((int(x, 2) + int(y, 2)))

problems = []

b_diff_reversed = binary_diff[::-1]
print(b_diff_reversed)
for i in range(len(str(b_diff_reversed))): 
    if str(b_diff_reversed)[i] == "1":
        problems.append("z" + str(i).zfill(2))

for p in problems:
    print(p)
    print(gates[p])


# binary adder. z23 and z39 are not XORs when they should be


# dbp <-> fdv because z06 was fdv XOR vjf. vjf looked fine, fdv was x06 AND y06, it should've been x06 XOR y06 which was fdv, so I swapped it
# kdf <-> z23 since nsr is x23 XOR y23 which should go into z23. It didn't it went into kdf
# z39 <-> rpp since vqr is x39 XOR y39 which should go into z39. It didn't it went into rpp
# z15 <-> ckj for same reason as above

# ckj,dbp,fdv,kdf,rpp,z15,z23,z39