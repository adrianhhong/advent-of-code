seeds_input, *rest = open("/Users/adrian.hong/Documents/advent-of-code/2023/day5/input.txt").read().split("\n\n")

seeds_input = list(map(int, seeds_input.split(":")[1].split()))
print(seeds_input)
seeds = []


for i in range(0, len(seeds_input), 2):
    seeds.append((seeds_input[i], seeds_input[i] + seeds_input[i + 1]))

print(seeds)

for mappings in rest:
    ranges = []

    # make the rest into arrays
    for line in mappings.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))

    new = []
    while len(seeds) > 0:
        start, end = seeds.pop()
        print(start,end)
        for dest, src, range_len in ranges:
            # find where the ranges overlap
            overlap_start = max(start, src)
            overlap_end = min(end, src + range_len)
            # if there is overlap
            if overlap_start < overlap_end:
                # we have an overlapping range. subtracting src gets offset
                new.append((overlap_start - src + dest, overlap_end - src + dest))
                # starting part we have not mapped. add it back into seeds to find that mapping in a future loop
                if overlap_start > start:
                    seeds.append((start, overlap_start))
                # ending part we have not mapped
                if end > overlap_end:
                    seeds.append((overlap_end, end))
                # break cause we have matched taht range
                break
        else:
            print('yep')
            new.append((start, end))
    seeds = new

print(min(seeds)[0])