import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input().rstrip())
std_like = []

std = input().rstrip().split()

for i in range(n):
    std[i] = [std[i], 0]

for _ in range(n):
    std_like.append(input().rstrip().split())

for l in range(n):
    sum = 0
    for j in range(n):
        for k in range(len(std_like[j])):
            if std_like[j][k] == std[l][0]:
                sum += 1
    std[l][1] = sum

std.sort(key=lambda x: -int(x[1]))

for a in range(n):
    print(*std[a])