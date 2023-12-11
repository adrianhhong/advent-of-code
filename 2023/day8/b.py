import math

(instructions_input, mapping_input)= open("input.txt").read().split('\n\n')
instructions = list(instructions_input)
mapping_input = mapping_input.split("\n")
mapping = {}
curr_keys = []

for i, line in enumerate(mapping_input):
    (k,v) = line.split(" = (")
    v2 = v.strip().split(',')
    mapping[k] = (v2[0], v2[1].strip().split(")")[0])
    if k.endswith("A"):
        curr_keys.append(k)

step = 0
steps_to_Z = []

# Every **A will only lead to one **Z.
# Just find how long every loop is and the LCM of all loops

while True:
    step_ind = step % len(instructions)
    ind = 0 if instructions[step_ind] == "L" else 1
    step += 1
    next_keys = []
    for k in curr_keys:
        next_key = mapping[k][ind]
        next_keys.append(next_key)
        print(next_keys)
        if next_key.endswith("Z"):
            steps_to_Z.append(step)
    if len(steps_to_Z) == len(curr_keys):
        break
    curr_keys = next_keys

print(step)
print(steps_to_Z)
print(math.lcm(*steps_to_Z))
