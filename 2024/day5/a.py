inputs = open(0).read().split('\n\n')

rules = {}
updates = []

for line in inputs[0].splitlines():
    string_rule = line.split('|')
    key = int(string_rule[0])
    value = int(string_rule[1])
    if key in rules:
        rules[key].append(value)
    else:
        rules[key] = [value]

for line in inputs[1].splitlines():
    string_rule = line.split(',')
    updates.append(list(map(int, string_rule)))

t=0

for u in updates:
    fail = False
    for i in range(len(u)-1,-1,-1): # start from the end of the updates array
        if u[i] not in rules:
            continue
        nums_after = rules[u[i]]
        for j in range(i-1, -1, -1): # take the next value from the end
            if u[j] in nums_after: # if that number should come after the ith number we break a rule
                fail = True
                break
    if fail == False:
        t += u[(len(u) - 1)//2]

print(t)