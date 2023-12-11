from functools import reduce

(time, distance )= open("input.txt").read().split('\n')
times = list(map(int, time.split(":")[1].split()))
distances = list(map(int, distance.split(":")[1].split()))

print(times)
print(distances)

#  dist_calc is all the iterations of all distances for all times
dist_calc = [ [] for _ in range(len(times)) ]

for i, t in enumerate(times):
    for r in range(t):
        speed = r
        time_left = t - r
        dist = time_left * speed
        dist_calc[i].append(dist)

ways_to_win = [0] * len(times)

for i in range(len(ways_to_win)):
    for d in range(len(dist_calc[i])):
        if dist_calc[i][d] > distances[i]:
            ways_to_win[i] += 1

print(ways_to_win)
print(reduce(lambda x, y: x*y, ways_to_win))