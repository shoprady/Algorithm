for _ in range(int(input())):
    s = list(input())
    for i in range(len(s)-1):
        if s[i]=='P' and s[i+1]=='O': s[i+1] = 'HO'
    print(''.join(s))