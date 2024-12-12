import math


input = list(map(int, open(0).read()))

print(input)

file = []

for i in range(math.ceil(len(input)/2)):
    for j in range(input[2*i]):
        file.append(i)
    if i == math.ceil(len(input)/2) -1 and len(input) % 2 != 0:
        break
    for k in range(input[2*i + 1]):
        file.append(".")

print(file)

def mov_loc(len_to_move, max_ind): # max_ind is the start index of the file to move
    dot_count = 0
    for i in range(max_ind):
        if file[i] == '.':
            dot_count += 1
            if dot_count == len_to_move:
                return i + 1 - dot_count
        else:
            dot_count = 0
    return -1

curr_num = file[len(file)-1]
num_count = 0
for i in range(len(file)-1, -1, -1):
    if file[i] != curr_num:
        # print(num_count)
        move_location = mov_loc(num_count, i+1)
        # print(move_location)
        if move_location != -1:
            for j in range(num_count):
                file[move_location+j], file[i+1+j] = file[i+1+j], file[move_location+j]
                # print(file)
        curr_num = file[i]
        num_count = 1           
    else:
        num_count += 1

print(file)
        
        
t=0
for i in range(len(file)):
    if file[i] == ".":
        continue
    t += i * int(file[i])

print(t)

# print(mov_loc(3, 10))     
