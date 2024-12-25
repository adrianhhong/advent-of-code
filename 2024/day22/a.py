
input = list(map(int, open(0).read().splitlines()))
print(input)

def mix(value, secret):
    return value ^ secret

def prune(value):
    return value % 16777216

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

for n in input:
    secret = n
    for _ in range(2000):
        secret = get_next_secret_number(secret)
    t += secret

print(t)