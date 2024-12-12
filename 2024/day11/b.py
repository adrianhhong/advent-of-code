from functools import cache  

input = list(map(int, open(0).read().split()))

t = 0

@cache
def count(v, iteration_left):
    if iteration_left == 0:
        return 1
    if v == 0:
        return count(1, iteration_left - 1)
    elif len(str(v)) % 2 == 0:
        dig = pow(10, (len(str(v)) // 2))
        a = v // dig
        b = v % dig
        return count(a, iteration_left-1) + count(b, iteration_left -1)
    else:
        return count(v*2024, iteration_left-1)


for v in input:
    t+=count(v, 75)

print(t)