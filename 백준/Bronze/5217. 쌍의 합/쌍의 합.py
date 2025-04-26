for _ in range(int(input())):
    n = int(input())
    ls = []
    for i in range(1, n // 2 + 1):
        if i != n - i:
            ls.append((i, n - i))
            
    if ls:
        print(f'Pairs for {n}:', end='')
    else:
        print(f'Pairs for {n}:')
        continue
        
    if len(ls) > 1:
        for k in range(len(ls) - 1):
            i, j = ls[k]
            print(f' {i} {j}', end=',')
    print(f' {ls[len(ls) - 1][0]} {ls[len(ls) - 1][1]}')