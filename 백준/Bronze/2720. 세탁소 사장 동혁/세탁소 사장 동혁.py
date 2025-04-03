for _ in range(int(input())):
    num = int(input())
    q = num // 25; num -= 25 * q
    d = num // 10; num -= 10 * d
    n = num // 5; num -= 5 * n
    print(q, d, n, num)