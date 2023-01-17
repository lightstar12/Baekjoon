import sys

nums = []

num_s = int(sys.stdin.readline())
for i in range(num_s):
    num = int(sys.stdin.readline())
    nums.append(num)

for l in range(len(nums)):
    for j in range(1, len(nums)):
        if nums[j] < nums[j - 1]:
            tmp = nums[j - 1]
            nums[j - 1] = nums[j]
            nums[j] = tmp
    
for k in range(len(nums)):
    print(nums[k])