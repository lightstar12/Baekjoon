import sys

n = int(sys.stdin.readline().strip())

for i in range(n):

    sen = sys.stdin.readline().strip()
    sum = 0

    for j in sen:
        if j == "(":
            sum += 1
        
        elif j == ")":
            sum -= 1
            if sum < 0:
                break

    if sum == 0:
        print("YES")
    else:
        print("NO")