import itertools


input = open(0).read().splitlines()

# print(input)

t = 0

for l in input:
    total, right = l.split(':')
    total = int(total)
    nums = list(map(int, right.split()))

    # print(nums)
    
    cart_product = list(itertools.product([0,1,2], repeat=len(nums)-1))

    for c in cart_product:
        running_total = nums[0]
        for i, s in enumerate(c):
            if s == 0:
                running_total += nums[i+1]
            elif s == 1:
                running_total *= nums[i+1]
            else:
                running_total = int(str(running_total) + str(nums[i+1]))
        if running_total == total:
            t += running_total
            break

print(t)
