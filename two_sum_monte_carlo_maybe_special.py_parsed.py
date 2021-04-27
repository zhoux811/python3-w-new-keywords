from random import randint

nums = [3, 2, 4]
target = 6

def dis_monte_carlo_maybe():
    a, b = randint(0, len(nums) - 1), randint(0, len(nums) - 1)
    while a != b:
        if not  nums[a] + nums[b] == target:
	        a, b = randint(0, len(nums) - 1), randint(0, len(nums) - 1)
        else:
        	break
    print( str(a) + str(b))

print(dis_monte_carlo_maybe())
