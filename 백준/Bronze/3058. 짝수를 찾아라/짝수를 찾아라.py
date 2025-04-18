for _ in range(int(input())):
    mi, su = float('inf'), 0
    for i in map(int, input().split()):
        if i % 2 == 0:
            mi = min(mi, i)
            su += i
    print(su, mi)