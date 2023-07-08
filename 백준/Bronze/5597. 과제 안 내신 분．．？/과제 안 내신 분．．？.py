from sys import stdin

input = stdin.readline

S = [0] * 30

for i in range(28):
    r = int(input())
    S[r - 1] = 1
    
for j in range(30):
    if S[j] == 0:
        print(j + 1)