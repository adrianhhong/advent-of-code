import z3

input = open("input.txt").read().split('\n')

hailstones = []
boundary = (200000000000000, 400000000000000)
# boundary = (7, 27)


for l in input:
    all = l.split("@")
    position = list(map(int, all[0].strip().split(",")))
    velocity = list(map(int, all[1].strip().split(",")))
    hailstones.append([position, velocity])

# z3 is a library to solve vector algebra
I = lambda name: z3.Real(name)

# positions and velocities of the perfect hailstone
x, y, z = I('x'), I('y'), I('z')
vx, vy, vz = I('vx'), I('vy'), I('vz')

s = z3.Solver()

for i, a in enumerate(hailstones):
	(xa, ya, za), (vxa, vya, vza) = a

	t = I(f't_{i}')
	s.add(t >= 0)
	s.add(x + vx * t == xa + vxa * t)
	s.add(y + vy * t == ya + vya * t)
	s.add(z + vz * t == za + vza * t)

assert s.check() == z3.sat

m = s.model()
x, y, z = m.eval(x), m.eval(y), m.eval(z)
x, y, z = x.as_long(), y.as_long(), z.as_long()

print(x, y, z)
print(x+y+z)