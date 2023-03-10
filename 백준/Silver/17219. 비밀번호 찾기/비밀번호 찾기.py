from sys import stdin

n, m = map(int, stdin.readline().rstrip().split())

passnum = {}

for _ in range(n):
    site, num = stdin.readline().split()
    passnum[site] = num

for _ in range(m):
    print(passnum[stdin.readline().rstrip()])