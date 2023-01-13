import sys

c = int(sys.stdin.readline())

tmp1 = input()
tmp1 = list(tmp1)

for i in range(c-1):
    tmp2 = input()
    for j in range(len(tmp1)):
        if tmp1[j] != tmp2[j]:
            tmp1[j] = '?'

print(''.join(tmp1))