from functools import cache

grid = []
broken_groups = []

lines = open("input.txt").read().split('\n')
for l in lines:
    (g, b) = l.split(' ')
    grid.append("?".join( [g]*5 ))
    broken_groups.append((tuple(map(int, b.split(','))))*5)

print(grid)
print(broken_groups)

# line: line we are processing e.g. ???.###
# broken_groups: e.g. 1,1,3
# pos: current character position of the line we are processing
# curr_count: current count of #s we are processing
# broken_group_pos: which broken_group we are currently processing
@cache
def get_perms(line, broken_groups, pos, curr_count, broken_group_pos):
    # base case: if we reach the end of the line i.e. the "." we added in the end
    if pos == len(line):
        # print('last')
        if broken_group_pos == len(broken_groups):
            return 1 # we found a valid case
        return 0
    
    # add 1 to curr_count if we meet another broken
    if line[pos] == "#":
        # print('#', pos, curr_count, broken_group_pos)
        return get_perms(line, broken_groups, pos+1, curr_count+1, broken_group_pos)

    if line[pos] == "." or broken_group_pos == len(broken_groups):
        # if we just saw a "#". check if curr_count is correct. if good, we move on
        if broken_group_pos < len(broken_groups) and curr_count == broken_groups[broken_group_pos]:
            return get_perms(line, broken_groups, pos+1, 0, broken_group_pos+1)
        # if we just saw a "." we only move the position
        elif curr_count == 0:
            return get_perms(line, broken_groups, pos+1, 0, broken_group_pos) 
        else:
            return 0

    if line[pos] == "?":
        # print("?", pos, curr_count, broken_group_pos)
        ## pretend it's a "#"
        # print('pretending #')
        hash_total = get_perms(line, broken_groups, pos+1, curr_count+1, broken_group_pos)
        # print('pretending .')

        dot_total = 0
        ## pretend it's a ".". this is the same as above but we only care about when it might result in a valid group

        # if we just saw a "#". check if curr_count is correct. if good, we move on
        if curr_count == broken_groups[broken_group_pos]:
            dot_total = get_perms(line, broken_groups, pos+1, 0, broken_group_pos+1)
        # if we just saw a "." we only move the position
        elif curr_count == 0:
            dot_total = get_perms(line, broken_groups, pos+1, 0, broken_group_pos)
        
        return (hash_total + dot_total)
    
    return 0 # this will never happen



num_perms_matching = 0

for i, l in enumerate(grid):
    print(broken_groups[i])
    print(l)
    perms = get_perms(l+".", broken_groups[i], 0, 0, 0) # add '.' at the end so we can reach base case.
    print(perms)
    num_perms_matching += perms

    # perms2 = getcount(l+".", broken_groups[i], 0, 0, 0) # add '.' at the end so we can reach base case.
    # print(perms2)
    

print(num_perms_matching)
                
