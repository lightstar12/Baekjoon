from sys import stdin

input = stdin.readline

N = int(input().rstrip())
nums = list(map(int, input().split()))
n = int(input().rstrip())
v = 0

for a in nums:
    if n == a:
        v = v + 1
        
print(v)