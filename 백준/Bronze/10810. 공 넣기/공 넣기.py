from sys import stdin

input = stdin.readline

N, M = map(int, input().split())
B = [0] * N

for a in range(M):
    i, j, k = map(int, input().split())
    for b in range(i-1 , j):
        B[b] = k
        
print(*B)