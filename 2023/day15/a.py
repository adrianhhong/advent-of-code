input = open("input.txt").read().split(',')

# print(input)

total = 0

for step in input:
    step_total = 0
    for c in step:
        step_total += ord(c)
        step_total *= 17
        step_total = step_total % 256
    
    total += step_total

print(total)
        