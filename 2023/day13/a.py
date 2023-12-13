grid = []

lines = open("input.txt").read().split('\n\n')
for l in lines:
    il = l.split('\n')
    grid.append(list(il))

# Create grid rotated anti-clockwise by 90 degrees
def rotate_matrix( m ):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]
rotated_grid = []

for p in grid:
    rotated_grid.append(rotate_matrix(p))


def patternColIsSame(newPattern, i, LPS):
    for c in newPattern:
        if c[i + 1 +LPS[i]] != c[i - 1 - LPS[i]]:
            return False
    return True

# Add ? in between every character
def UpdatedString(string):
    newString = ['?']
    for char in string:
        newString += [char, '?']
    return ''.join(newString)

# Use Manachen algorithm https://www.educative.io/answers/longest-palindromic-substring-in-on-with-manachers-algorithm
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
        if R > i:
            LPS[i] = min(R-i, LPS[iMirror])
        else:
            LPS[i] = 0
        try:
            # Changed this to check if the column is the same
            while patternColIsSame(newPattern, i, LPS):
                LPS[i] += 1
        except:
            pass
        
        if i + LPS[i] > R:
            C = i
            R = i + LPS[i]
    
    del LPS[1::2] # delete every odd element in list cause we only want mirrors between characters. odd elements are if the column itself is a mirror.

    # r is the max palendrome, c is the number before the index it is at. if c is 2 then it would where the v is: #.v.# THERE CAN BE MORE THAN ONE LOCATION FOR C SO ITS A TUPLE
    r, c = max(LPS), [i for i, x in enumerate(LPS) if x == max(LPS)]

    # for every mirror, check if it actually reaches either end of the grid
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