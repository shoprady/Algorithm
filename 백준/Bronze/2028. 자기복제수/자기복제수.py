for _ in range(int(input())):
    n = int(input())
    nn, n = str(n * n), str(n)
    check = True
    for i in range(len(n)):
        if n[-1-i] != nn[-1-i]:
            print('NO')
            check = False
            break
    if check: print('YES')