for _ in range(int(input())):
    a, b, c = map(int, input().split())
    ans = 0
    for x in range(1, a + 1):
        for y in range(1, b + 1):
            for z in range(1, c + 1):
                if x%y == y%z == z%x:
                    ans += 1
    print(ans)