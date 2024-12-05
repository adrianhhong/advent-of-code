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

bad_updates = []

for u in updates:
    fail = False
    for i in range(len(u)-1,-1,-1):
        if u[i] not in rules:
            continue
        nums_after = rules[u[i]]
        for j in range(i-1, -1, -1):
            if u[j] in nums_after:
                fail = True
    if fail == True:
        bad_updates.append(u)


def swap_bad(u):
    for i in range(len(u)-1,-1,-1):
        if u[i] not in rules:
            continue
        after_values = rules[u[i]]
        for j in range(i-1, -1, -1):
            if u[j] in after_values:
                u[i], u[j] = u[j], u[i] # swap the two numbers that break a rule
                return False
    return True

print(bad_updates)
t=0

for u in bad_updates: # in all the updates that are in error
    while not swap_bad(u): # keep swapping until there are no numbers breaking any rules
        True    
    t += u[(len(u) - 1)//2]

print(t)
