import sys

letter = sys.stdin.readline()
i = 0
count = 0

while(i < (len(letter)- 1)):

    if letter[i] == 'c' and (letter[i + 1] == '=' or letter[i + 1] == '-'):
        count = count + 1
        i = i + 2

    elif letter[i] == 'd' and letter[i + 1] == '-':
        count = count + 1
        i = i + 2

    elif letter[i] == 'd' and letter[i + 1] == 'z' and letter[i + 2] == '=':
        count = count + 1
        i = i + 3

    elif letter[i] == 'l' and letter[i + 1] == 'j':
        count = count + 1
        i = i + 2

    elif letter[i] == 'n' and letter[i + 1] == 'j':
        count = count + 1
        i = i + 2

    elif letter[i] == 's' and letter[i + 1] == '=':
        count = count + 1
        i = i + 2

    elif letter[i] == 'z' and letter[i + 1] == '=':
        count = count + 1
        i = i + 2

    else:
        count = count + 1
        i = i + 1

print(count)