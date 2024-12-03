import re

l = open(0).read()

print(l)

matches = re.findall(r'mul\([1-9]\d*,[1-9]\d*\)', l)
print(matches)

t = 0

for m in matches:
    nums = re.findall(r'[1-9]\d*', m)
    print(nums)
    t += int(nums[0]) * int(nums[1])

print(t)