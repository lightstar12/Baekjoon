import sys

case = int(sys.stdin.readline())

for i in range(case):
    result = sys.stdin.readline()
    score = 0
    plus_score = 1
    for j in range(len(result)):
        if result[j] == 'O':
            if result[j - 1] == 'O':
                if j == 0:
                    continue
                plus_score = plus_score + 1
            
            score = score + plus_score
        elif result[j] == 'X':
            plus_score = 1
            continue
    
    print(score)