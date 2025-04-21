while True:
    a, b = map(int, input().split())
    if a == b == 0: break
    diff, tmp, i = 0, abs(a - 1), 2
    while True:
        diff = abs(a - i ** b)
        if diff > tmp: break
        else:
            tmp = diff
            i += 1
    print(i - 1)