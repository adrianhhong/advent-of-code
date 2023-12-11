
(time_input, distance_input )= open("input.txt").read().split('\n')
time = int(time_input.split(":")[1].replace(" ", ""))
distance = int(distance_input.split(":")[1].replace(" ", ""))

print(time)
print(distance)

# too time consuming to find all results... so find the break points
break_points= []

# find the starting break point where after that point you will win
for r in range(time):
    speed = r
    time_left = time - r
    dist = time_left * speed
    if dist > distance:
        break_points.append(r)
        break

# find the ending break point where before that point you will win
for r in range(time, -1, -1):
    speed = r
    time_left = time - r
    dist = time_left * speed
    if dist > distance:
        break_points.append(r)
        break

print(break_points)
print(break_points[1]- break_points[0]+1) # inclusive of the last one
