input = open("input.txt").read().split('\n')



# u, r, d, l
dir = ["u", "r", "d", "l"]
x_dir = [0, 1, 0, -1]
y_dir = [-1, 0, 1, 0]
b_slash_x = [-1, 0, 1, 0]
b_slash_y = [0, 1, 0, -1]
b_slash_dir = ["l", "d", "r", "u"]
f_slash_x = [1, 0, -1, 0]
f_slash_y = [0, -1, 0, 1]
f_slash_dir = ["r", "u", "l", "d"]

pipe_dir = [("u"), ("u", "d"), ("d"), ("u", "d")]
hyph_dir = [("l", "r"), ("r"), ("l", "r"), ("l")]



def is_inside_grid(position):
    if 0 <= position[0] < len(input) and 0 <= position[1] < len(input[0]):
        return True
    return False


def get_next_beams(beam):
    # print(beam)

    beam_grid[beam[0]][beam[1]] = 1
    # print(beam_grid)
    d_index = dir.index(beam[2])
    current_symbol = input[beam[0]][beam[1]]
    
    next_beams = []

    if current_symbol == '.':
        next_pos = [beam[0]+y_dir[d_index], beam[1]+x_dir[d_index]]
        if is_inside_grid(next_pos):
            next_beams.append((next_pos[0], next_pos[1], beam[2]))
    elif current_symbol == '\\':
        next_pos = [beam[0]+b_slash_y[d_index], beam[1]+b_slash_x[d_index]]
        if is_inside_grid(next_pos):
            next_beams.append((next_pos[0], next_pos[1], b_slash_dir[d_index]))
    elif current_symbol == '/':
        next_pos = [beam[0]+f_slash_y[d_index], beam[1]+f_slash_x[d_index]]
        if is_inside_grid(next_pos):
            next_beams.append((next_pos[0], next_pos[1], f_slash_dir[d_index]))
    elif current_symbol == '|':
        next_beams = []
        pipe_dirs = pipe_dir[d_index]
        for p in pipe_dirs:
            index = dir.index(p)
            next_pos = [beam[0]+y_dir[index], beam[1]+x_dir[index]]
            if is_inside_grid(next_pos):
                next_beams.append((next_pos[0], next_pos[1], p))
    elif current_symbol == '-':
        hyph_dirs = hyph_dir[d_index]
        for p in hyph_dirs:
            index = dir.index(p)
            next_pos = [beam[0]+y_dir[index], beam[1]+x_dir[index]]
            if is_inside_grid(next_pos):
                next_beams.append((next_pos[0], next_pos[1], p))
    

    return next_beams

all_entrances = []
for i in [(0, "d"), (len(input)-1, "u")]:
    for j in range(len(input[0])):
        all_entrances.append((i[0], j, i[1]))

for i in range(len(input)):
    for j in [(0, "r"), (len(input[0])-1, "l")]:
        all_entrances.append((i, j[0], j[1]))

print(all_entrances)
print(len(all_entrances))
highest_total = 0

for it, e in enumerate(all_entrances):
    print(it)
    print(e)
    beam_grid = [[0 for i in range(len(input))] for j in range(len(input[0]))]

    all_beams_seen = [e]
    beams = [e]

    while beams:
        next = get_next_beams(beams.pop())
        for n in next:
            if n not in all_beams_seen:
                all_beams_seen.append(n)
                beams.append(n)

    total = 0
    
    for i in beam_grid:
        for j in i:
            if j:
                total += 1
    if total > highest_total:
        highest_total = total

    print('t',total)
    

# print(beam_grid)
print(highest_total)