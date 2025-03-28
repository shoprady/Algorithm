for _ in range(int(input())):
    input()
    n, tmp = int(input()), 0
    for _ in range(n):
        tmp += int(input())
    if tmp % n == 0: print('YES')
    else: print('NO')