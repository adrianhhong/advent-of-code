import re

total = 0

with open('input.txt') as input:
    for line in input:
        first_digit = re.findall(r'\d', line)[0]
        last_digit = re.findall(r'\d', line)[-1]
        total += int(first_digit+last_digit)

print(total)
