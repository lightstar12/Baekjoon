s = ""
while True:
    s = input()
    if s == '#':
        break
    c = 0
    for i in range(len(s)):
        if s[i] == 'A' or s[i] == 'E' or s[i] == 'I' or s[i] == 'O' or s[i] == 'U' or s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
            c = c + 1
    print(c)