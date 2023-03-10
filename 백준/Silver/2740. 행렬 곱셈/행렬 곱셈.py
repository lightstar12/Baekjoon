from sys import stdin

input = stdin.readline

def array_mux(a_a, b_a, a, b):
    a_sum = 0
    for i in range(len(b_a)):
        a_sum += a_a[a][i] * b_a[i][b]
    
    return a_sum


a_n, a_m = map(int, input().rstrip().split())

a_array = [[0 for _ in range(a_m)] for _ in range(a_n)]


for i in range(a_n):
    a_array[i] = list(map(int, input().rstrip().split()))

b_n, b_m = map(int, input().rstrip().split())

b_array = [[0 for _ in range(b_m)] for _ in range(b_n)]

for j in range(b_n):
    b_array[j] = list(map(int, input().rstrip().split()))

c_n = a_n
c_m = b_m

c_array = [[0 for _ in range(c_m)] for _ in range(c_n)]

for k in range(c_n):
    for l in range(c_m):
        c_array[k][l] = array_mux(a_array, b_array, k, l)

for p in range(len(c_array)):
    print(*c_array[p])