import re

lines_list = open(0).read().splitlines()
l=[]
for line in lines_list:
    print(line)
    l.append(list(map(int,line.split(" "))))


t = 0

for ln in l:
    diff = []
    for i in range(len(ln)):
        if i==0:
            continue
        else:
            diff.append(ln[i-1] - ln[i])
    print(diff)
    if (all([x > 0 for x in diff]) or  all([x < 0 for x in diff])):
        if (all([abs(x) < 4 for x in diff])):
            t += 1

print(t)