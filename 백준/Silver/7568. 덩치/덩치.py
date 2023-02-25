import sys

n = int(sys.stdin.readline().rstrip())

weight = []
height = []
chi = [1] * n

for i in range(n):
    w, h = map(int, sys.stdin.readline().rstrip().split())
    weight.append(w)
    height.append(h)


for j in range(n):
    for k in range(n):
        if j == k:
            continue
        if weight[j] < weight[k] and height[j] < height[k]:
            chi[j] += 1

print(*chi)