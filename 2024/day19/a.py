from functools import cache

s, p = open(0).read().split('\n\n')
towels = s.split(", ")
designs = p.splitlines()

@cache
def dynamic(substring):
    if substring == "":
        return True

    for t in towels:
        if substring.startswith(t):
            if dynamic(substring[len(t):]):
                return True
    
    return False

t = 0

for d in designs:
    if dynamic(d):
        t += 1

print(t)