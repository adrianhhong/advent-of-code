from functools import cache

s, p = open(0).read().split('\n\n')
towels = s.split(", ")
designs = p.splitlines()

@cache
def dynamic(substring):
    if substring == "":
        return 1

    num_ways = 0

    for t in towels:
        if substring.startswith(t):
            num_ways += dynamic(substring[len(t):])
    
    return num_ways

t = 0

for d in designs:
    t += dynamic(d)

print(t)