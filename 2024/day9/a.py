import math


input = list(map(int, open(0).read()))

print(input)

file = []

for i in range(math.ceil(len(input)/2)):
    for j in range(input[2*i]):
        file.append(i)
    if i == math.ceil(len(input)/2) -1 and len(input) % 2 != 0:
        break
    for k in range(input[2*i + 1]):
        file.append(".")

print(file)

p1 = 0
p2 = len(file)-1

def is_done(next_p1):
    for p in range(next_p1, len(file)):
        if file[p] != ".":
            return False
    return True


while True:
    while file[p1] != ".":
        p1 += 1
    while file[p2] == ".":
        p2 -= 1
    file[p1], file[p2] = file[p2], file[p1]
    next_p1 = p1
    while file[next_p1] != ".":
        next_p1 += 1
    if is_done(next_p1):
        print(next_p1,p2)
        break


print(file)
t=0
for i in range(len(file)):
    if file[i] == ".":
        break
    t += i * int(file[i])

print(t)