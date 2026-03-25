for _ in range(int(input())):
    a, n = map(int, input().split())
    new, i = [], 1
    while i <= a//n:
        i *= n
    while i > 0:
        tmp = a//i
        if tmp > 9: new.append(chr(tmp+55))
        else: new.append(str(tmp))
        a -= tmp * i
        i //= n
    new = ''.join(new)
    print(1) if new==new[::-1] else print(0)