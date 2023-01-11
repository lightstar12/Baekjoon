import sys

for j in range(3):
    c = int(sys.stdin.readline())
    num = 0
    for i in range(c):
        innum = int(sys.stdin.readline())
        num = num + innum
    if num == 0:
        print(0)
    elif num > 0:
        print('+')
    else:
        print('-')