from random import randint

nums = [3, 2, 4]
target = 6

def dis_monte_carlo_maybe():
    a, b = randint(0, len(nums) - 1), randint(0, len(nums) - 1)
    while a != b:
        a, b = randint(0, len(nums) - 1), randint(0, len(nums) - 1) unless  nums[a] + nums[b] == target
    print( str(a) + str(b))

print(dis_monte_carlo_maybe())
