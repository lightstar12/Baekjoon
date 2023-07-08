from sys import stdin

input = stdin.readline

N, M = map(int, input().split())

B = [0] * N
for a in range(N):
    B[a] = a + 1

for b in range(M):
    i, j = map(int, input().split())
    tmp = B[i - 1]
    B[i - 1] = B[j - 1]
    B[j - 1] = tmp

print(*B)