import re

l = open(0).read()

print(l)

matches = re.findall(r'mul\([1-9]\d*,[1-9]\d*\)|do\(\)|don\'t\(\)', l)
print(matches)

t = 0

enabled = True

for m in matches:
    if re.findall(r'do\(\)', m):
        enabled = True
    elif re.findall(r'don\'t\(\)', m):
        enabled = False
    else:
        if (enabled):
            nums = re.findall(r'[1-9]\d*', m)
            print(nums)
            t += int(nums[0]) * int(nums[1])

print(t)