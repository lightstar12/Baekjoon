import sys
sys.setrecursionlimit(10**5)

def Fib(a):
    if a == 0:
        return 0
    
    elif a == 1:
        return 1

    else:
        result = 0
        result = result + Fib(a - 1) + Fib(a - 2)
        return result
    
n = int(sys.stdin.readline().rstrip())

print(Fib(n))