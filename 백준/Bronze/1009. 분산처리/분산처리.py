import sys

c = int(sys.stdin.readline())

for i in range(c):
    base, power = input().split()
    base = int(base)
    power = int(power)

    if base % 10 == 0:
        print(10)
    else:
        base = base % 10
        
        if base == 1 or base == 5 or base == 6:
            print(base % 10)
        elif base == 4 or base == 9:
            if power % 2 == 1:
                print(base % 10)
            elif power % 2 == 0:
                print((base * base) % 10)
        elif base == 2 or base == 3 or base == 7 or base == 8:
            if power % 4 == 1:
                print(base % 10)
            elif power % 4 == 2:
                print((base * base) % 10)
            elif power % 4 == 3:
                print((base * base * base) % 10)
            elif power % 4 == 0:
                print((base * base * base * base) % 10)
