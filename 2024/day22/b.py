from functools import cache

input = list(map(int, open(0).read().splitlines()))
print(input)

def mix(value, secret):
    return value ^ secret

def prune(value):
    return value % 16777216

@cache
def get_next_secret_number(n):
    secret_num = n
    n *= 64
    n = prune(mix(n, secret_num))
    secret_num = n
    n = n // 32
    n = prune(mix(n, secret_num))
    secret_num = n
    n = n * 2048
    return prune(mix(n, secret_num))

t = 0

diff_map = {}

for n in input:
    sequence = [n % 10]
    secret = n
    for _ in range(2000):
        secret = get_next_secret_number(secret)
        sequence.append(secret % 10)
    seen = set()
    for i in range(4,len(sequence)):
        key = (sequence[i-4] - sequence[i-3], sequence[i-3] - sequence[i-2], sequence[i-2] - sequence[i-1], sequence[i-1] - sequence[i])
        value = sequence[i]
        if key in seen:
            continue
        seen.add(key)
        if key not in diff_map:
            diff_map[key] = value
        else:
            diff_map[key] += value

print(max(diff_map.values()))