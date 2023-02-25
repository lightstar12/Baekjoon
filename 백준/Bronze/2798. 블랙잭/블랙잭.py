import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

num = list(map(int, sys.stdin.readline().rstrip().split()))

cha = 300000
ans = 0

for i in range(len(num)):
    for j in range(i+1, len(num)):
        for l in range(j+1, len(num)):
            sum = num[i] + num[j] + num[l]
            if cha > abs(k - sum) and sum <= k:
                cha = abs(k - sum)
                ans = sum

print(ans)