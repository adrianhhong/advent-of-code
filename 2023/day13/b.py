grid = []

lines = open("input.txt").read().split('\n\n')
for l in lines:
    il = l.split('\n')
    grid.append(list(il))

def rotate_matrix( m ):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]

rotated_grid = []

for p in grid:
    rotated_grid.append(rotate_matrix(p))


# -1: not same, 1: off by 1 smudge, 0: exact same
def patternColIsSameWithErrors(newPattern, i, LPS):
    errors = 0
    for c in newPattern:
        if c[i + 1 +LPS[i]] != c[i - 1 - LPS[i]]:
            errors += 1
            if (errors == 2):
                return -1
    if errors == 1:
        return 1
    return 0


def UpdatedString(string):
    newString = ['?']
    for char in string:
        newString += [char, '?']
    return ''.join(newString)

def Manachen(pattern):
    newPattern = []
    oldPattern = []
    for p in pattern:
        oldPattern = p
        newPattern.append(UpdatedString(p))

    LPS = [0 for _ in range(len(newPattern[0]))]
    C = 0
    R = 0
    for i in range(len(newPattern[0])):
        iMirror = 2*C - i
        smudges_used = 0

        if R > i:
            LPS[i] = min(R-i, LPS[iMirror])
        else:
            LPS[i] = 0
        try:
            # changed this to check if columns are the same or off by 1 smudge
            while True:
                same = patternColIsSameWithErrors(newPattern, i, LPS)
                if same == -1:
                    break
                if same == 1:
                    smudges_used += 1
                    if smudges_used == 2:
                        break
                LPS[i] += 1
        except:
            pass

        # since there is 1 answer for when the mirror makes the exact same on both sides
        # we can get rid of this, since we ALWAYS want a new answer that HAS to use the 1 smudge error correction
        if smudges_used == 0 :
            LPS[i] = 0
        else:
            if i + LPS[i] > R:
                C = i
                R = i + LPS[i]
            
    
    
    del LPS[1::2] # delete every odd element in list cause we only want mirrors between characters

    # r is the max palendrome, c is the number before the index it is at. if c is 2 then it would where the v is: #.v.# THERE CAN BE MORE THAN ONE LOCATION FOR C SO ITS A TUPLE
    r, c = max(LPS), [i for i, x in enumerate(LPS) if x == max(LPS)]

    for index, v in enumerate(LPS):
        if v != 0:
            pal_reaches_left = index - v/2 <= 0
            pal_reaches_right = (index-1 + (v/2)) >= len(oldPattern)-1
            if pal_reaches_left or pal_reaches_right:
                return index

    return 0
    

total = 0

for p in grid:
    total += Manachen(p)

for p in rotated_grid:
    total += Manachen(p)* 100

    
print(total)