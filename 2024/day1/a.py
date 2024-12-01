left = []
right = []

lines_list = open(0).read().splitlines()

for line in lines_list:
    split_line = line.split("   ")
    left.append(int(split_line[0]))
    right.append(int(split_line[1]))

left.sort()
right.sort()

total = 0

for i in range(len(left)):
    total += abs(left[i] - right[i])

print(total)