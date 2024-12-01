left = []

right_freq = {}

lines_list = open(0).read().splitlines()

for line in lines_list:
    split_line = line.split("   ")
    left.append((split_line[0]))
    if (split_line[1] in right_freq):
        right_freq[split_line[1]] += 1
    else:
        right_freq[split_line[1]] = 1

total = 0

for i in range(len(left)):
    if left[i] in right_freq:
        total += int(left[i]) * right_freq[left[i]]

print(total)