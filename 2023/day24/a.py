input = open("input.txt").read().split('\n')

hailstones = []
boundary = (200000000000000, 400000000000000)
# boundary = (7, 27)


for l in input:
    all = l.split("@")
    position = list(map(int, all[0].strip().split(",")))
    velocity = list(map(int, all[1].strip().split(",")))
    hailstones.append([position, velocity])

def get_lines(hailstone):
    position, velocity = hailstone
    x, y, z  = position
    vx, vy, vz = velocity
    m = vy / vx
    c = y - m*x
    return (m, c)

def in_the_future(hailstone_a, hailstone_b, intersection_x, intersection_y):
    vxa = hailstone_a[1][0]
    xa = hailstone_a[0][0]
    vya = hailstone_a[1][1]
    ya = hailstone_a[0][1]
    vxa_pos = vxa > 0
    inxa_pos = intersection_x > xa
    vya_pos = vya > 0
    inya_pos = intersection_y > ya
    vxb = hailstone_b[1][0]
    xb = hailstone_b[0][0]
    vyb = hailstone_b[1][1]
    yb = hailstone_b[0][1]
    vxb_pos = vxb > 0
    inxb_pos = intersection_x > xb
    vyb_pos = vyb > 0
    inyb_pos = intersection_y > yb
    if (vxa_pos == inxa_pos) and (vya_pos == inya_pos) and (vxb_pos == inxb_pos) and (vyb_pos == inyb_pos):
        return True
    return False



def will_collide(hailstone_a, hailstone_b):
    ma, ca = get_lines(hailstone_a)
    mb, cb = get_lines(hailstone_b)

    if ma - mb == 0:
        return False # won't collide because parallel
    intersection_x = (cb - ca) / (ma - mb)
    intersection_y = ma * intersection_x + ca
    if (boundary[0] <= intersection_x < boundary[1]) and (boundary[0] <= intersection_y < boundary[1]):
        if in_the_future(hailstone_a, hailstone_b, intersection_x, intersection_y):
            return True
    return False


total = 0
for i in range(len(hailstones)):
    for j in range(i+1, len(hailstones)):
        if will_collide(hailstones[i], hailstones[j]):
            print('yes', hailstones[i], hailstones[j])
            total += 1

print(total)