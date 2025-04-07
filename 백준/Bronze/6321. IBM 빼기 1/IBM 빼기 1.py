for i in range(1, int(input()) + 1):
    s = input()
    print('String #{0}'.format(i))
    for j in s:
        c = ord(j) + 1
        print(chr(c), end='') if c <= 90 else print(chr(c - 26), end='')
    print()
    print()