import sys
from collections import deque

Queue = deque()

n = int(sys.stdin.readline().strip())

for i in range(n):
    cmd = sys.stdin.readline().strip().split()

    if cmd[0] == 'push':
        Queue.append(cmd[1])

    elif cmd[0] == 'pop':
        if len(Queue) == 0:
            print(-1)
        else:
            print(Queue.popleft())

    elif cmd[0] == 'size':
        print(len(Queue))

    elif cmd[0] == 'empty':
        if len(Queue) == 0:
            print(1)
        else:
            print(0)

    elif cmd[0] == 'front':
        if len(Queue) == 0:
            print(-1)
        else:
            print(Queue[0])

    elif cmd[0] == 'back':
        if len(Queue) == 0:
            print(-1)
        else:
            print(Queue[len(Queue) - 1])