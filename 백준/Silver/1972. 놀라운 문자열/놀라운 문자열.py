from sys import stdin

while(1):
    sp = stdin.readline().rstrip()
    abbreak = True
    
    if sp == '*':
        break
    
    if len(sp) == 1 or len(sp) == 2:
        print(sp, 'is surprising.')
    
    else:
        for i in range(1, len(sp)):
            li_D = []
            for j in range(len(sp) - i):
                li_d = sp[j]+sp[j+i]
                li_D.append(li_d)
            if len(li_D) != len(set(li_D)):
                abbreak = False
                print(sp, 'is NOT surprising.')
                break
        if abbreak == False:
            continue
        print(sp, 'is surprising.')