
input = list(map(int, open(0).read().split()))


def flatten(xss):
    flat_list = []
    for xs in xss:
        if isinstance(xs, list):
            for x in xs:
                flat_list.append(x)
        else:
            flat_list.append(xs)
    return flat_list

for r in range(25):
    for i, v in enumerate(input):
        if v == 0:
            input[i] = 1
        elif len(str(v)) % 2 == 0:
            dig = pow(10, (len(str(v)) // 2))
            a = v // dig
            b = v % dig
            input[i] = [a,b]
        else:
            input[i] = v * 2024
    print(input)
    input = flatten(input)

print(len(input))