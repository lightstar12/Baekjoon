import sys
sys.setrecursionlimit(10**7)

nums = []

for i in range(10000):
    nums.append(i + 1)

def self_number(n, numbers):
    if n > 10000:
        return 0
    else:
        n = n + int((n / 1000)) + (int((n / 100)) % 10) + (int((n / 10)) % 10) + int((n % 10))
        if n > 10000:
            return 0
        numbers[n - 1] = 0
        self_number(n, numbers)

for j in range(10000):
    self_number(j + 1, nums)

for k in range(10000):
    if nums[k] != 0:
        print(nums[k])