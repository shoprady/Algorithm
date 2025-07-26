for _ in range(int(input())):
    a, b, x, c, d, y = map(int, input().split())
    r = ((a-c) ** 2 + (b-d) ** 2) ** 0.5
    if r == 0:
        if x == y:
            print(-1)
        else:
            print(0)
    elif x-y == r or y-x == r or x+y == r:
        print(1)
    elif x+y < r:
        print(0)
    elif x-y > r or y-x > r:
        print(0)
    else:
        print(2)