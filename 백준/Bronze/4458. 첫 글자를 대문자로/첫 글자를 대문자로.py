for _ in range(int(input())):
    s = list(input())
    if s[0].islower():
        s[0] = s[0].upper()
    print(''.join(s))