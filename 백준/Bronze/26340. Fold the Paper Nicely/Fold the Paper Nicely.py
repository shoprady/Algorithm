for _ in range(int(input())):
    a, b, k = map(int, input().split())
    print(f'Data set: {a} {b} {k}')
    for _ in range(k):
        if a > b: a //= 2
        else: b //= 2
    if b > a: a, b = b, a
    print(f'{a} {b}')
    print()