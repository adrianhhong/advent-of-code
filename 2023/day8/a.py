(instructions_input, mapping_input)= open("input.txt").read().split('\n\n')
instructions = list(instructions_input)
mapping_input = mapping_input.split("\n")
mapping = {}


for i, line in enumerate(mapping_input):
    (k,v) = line.split(" = (")
    v2 = v.strip().split(',')
    mapping[k] = (v2[0], v2[1].strip().split(")")[0])

step = 0
curr_key = "AAA"

while True:
    step_ind = step % len(instructions)
    ind = 0 if instructions[step_ind] == "L" else 1
    next_key = mapping[curr_key][ind]
    step += 1
    if next_key == "ZZZ":
        break
    curr_key = next_key

print(step)