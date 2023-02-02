import sys

Stack = []
n = int(sys.stdin.readline().strip())

for i in range(n):
    cmd = sys.stdin.readline().strip().split()

    if cmd[0] == 'push':
        Stack.append(cmd[1])

    elif cmd[0] == 'pop':
        if len(Stack) == 0:
            print(-1)
        else:
            print(Stack.pop())
     
    elif cmd[0] == 'size':
        print(len(Stack))

    elif cmd[0] == 'empty':
        if len(Stack) == 0:
            print(1)
        else:
            print(0)
    
    elif cmd[0] == 'top':
        if len(Stack) == 0:
            print(-1)
        else:
            print(Stack[len(Stack) - 1])
