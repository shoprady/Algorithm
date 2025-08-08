for _ in range(int(input())):
    p = input().split()
    ls = input().split()
    if p[1] == 'C':
        for i in range(len(ls)):
            print(ord(ls[i])-64, end=' ')
    else:
        for i in range(len(ls)):
            print(chr(int(ls[i])+64), end=' ')
    print('')