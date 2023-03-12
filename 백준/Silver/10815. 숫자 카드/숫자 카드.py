from sys import stdin
from bisect import bisect_left
from bisect import bisect_right
input = stdin.readline

n = int(input().rstrip())
n_card = [0] * n
n_card = list(map(int, input().rstrip().split()))

n_card.sort()

m = int(input().rstrip())
m_card = [0] * m
m_card = list(map(int, input().rstrip().split()))

ans = [0] * m
for i in range(m):
   if bisect_left(n_card, m_card[i]) != bisect_right(n_card, m_card[i]):
      ans[i] = 1

print(*ans)