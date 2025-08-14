while True:
    s = input()
    if s == '*': break
    tmp = ord(s[0])-65 if 65 <= ord(s[0]) <= 90 else ord(s[0])-97
    s = s.split()
    check = True
    for i in s:
        c = ord(i[0])-65 if 65 <= ord(i[0]) <= 90 else ord(i[0])-97
        if c == tmp:
            tmp = c
        else:
            check = False
            break
    print('Y') if check else print('N')