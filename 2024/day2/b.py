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
    if (all([x > 0 for x in diff]) or  all([x < 0 for x in diff])) and (all([abs(x) < 4 for x in diff])):
        t += 1
    else:
        print ('hi')
        for dind in range(len(ln)):
            newln = [i for i in ln]
            newln.pop(dind)
            print(newln)
            newdiff = []
            for i in range(len(newln)):
                if i==0:
                    continue
                else:
                    newdiff.append(newln[i-1] - newln[i])
            if (all([x > 0 for x in newdiff]) or  all([x < 0 for x in newdiff])) and (all([abs(x) < 4 for x in newdiff])):
                t += 1
                print('yes')
                break

print(t)
