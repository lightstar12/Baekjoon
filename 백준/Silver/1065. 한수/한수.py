import sys
sys.setrecursionlimit(10**7)

N = int(sys.stdin.readline())
count = 0

for i in range(N):
    i = i + 1
    if i < 10:
        count = count + 1
    elif i < 100:
        count = count + 1
    elif i < 1000:
        if (int(i / 100) - (int(i / 10) % 10)) == ((int(i / 10) % 10) - i % 10):
            count = count + 1

print(count)