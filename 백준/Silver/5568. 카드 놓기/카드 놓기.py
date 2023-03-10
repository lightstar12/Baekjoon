import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input().rstrip())
k = int(input().rstrip())

num = []
number = []

for _ in range(n):
    num.append(input().rstrip())

for i in permutations(num, k):
    number.append(list(i))

for j in range(len(number)):
    number[j] = ''.join(number[j])

number = list(set(number))

print(len(number))