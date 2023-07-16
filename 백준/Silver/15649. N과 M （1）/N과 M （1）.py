from sys import stdin
from itertools import permutations

input = stdin.readline

N, M = map(int, input().split())

lists = [0] * N
for i in range(N):
    lists[i] = i + 1
    
a = list(permutations(lists, M))

for j in range(len(a)):
    print(*a[j])