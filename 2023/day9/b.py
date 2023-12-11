histories = []
extraps = []

hs = open("input.txt").read().split('\n')
for h in hs:
    histories.append(list(map(int, h.split(" "))))


for h in histories:
    diffs_stack = [h]
    prev_diffs = h

    for l in range(len(h)):
        curr_diffs = []
        # create curr_diffs
        for i in range(0, len(prev_diffs)-1):
            curr_diffs.append(prev_diffs[i+1] - prev_diffs[i])
        diffs_stack.insert(0, curr_diffs)

        if all(v == 0 for v in curr_diffs):
            break
        prev_diffs = curr_diffs

    diffs_stack[0].insert(0, 0)

    for i in range(0, len(diffs_stack)-1):
        diffs_stack[i+1].insert(0, diffs_stack[i+1][0] - diffs_stack[i][0])
        
    extraps.append(diffs_stack[-1][0])
    

print(sum(extraps))