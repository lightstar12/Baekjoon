from sys import stdin

input = stdin.readline

X = int(input().rstrip())
N = int(input().rstrip())
sum = 0
for i in range(N):
    a, b = map(int, input().split())
    sum = sum + a * b

if X == sum:
    print("Yes")
else:
    print("No")  