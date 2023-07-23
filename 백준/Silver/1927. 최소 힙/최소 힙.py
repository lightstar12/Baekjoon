from sys import stdin
import heapq

input = stdin.readline

N = int(input())
Heap = []
for i in range(N):
    x = int(input())
    if x == 0:
        if len(Heap) == 0:
            print('0')
        else:
            print(heapq.heappop(Heap))
    elif x > 0:
        heapq.heappush(Heap, x)