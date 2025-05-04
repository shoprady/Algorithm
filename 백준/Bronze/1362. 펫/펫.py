i = 1
while True:
    o, w = map(int, input().split())
    if o == w == 0:
        break
        
    check = False
    while True:
        s, n = input().split()
        n = int(n)
        if s == 'E':
            w -= n
            if w <= 0:
                check = True
        elif s == 'F':
            w += n
        else: break
        
    if check:
        print(f'{i} RIP')
    elif o/2 < w < o*2:
        print(f'{i} :-)')
    else:
        print(f'{i} :-(')
    i += 1