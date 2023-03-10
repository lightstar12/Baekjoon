from sys import stdin
from itertools import combinations

n, s = map(int, stdin.readline().split())

li = list(map(int, stdin.readline().split()))

sum_ = []
for j in range(1, n + 1):
    for k in combinations(li, j):
        sum_.append(sum(k))

case_ = 0

for l in sum_:
    if s == l:
        case_ += 1

print(case_)