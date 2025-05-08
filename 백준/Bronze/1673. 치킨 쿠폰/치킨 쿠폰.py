while True:
    try:
        n, k = map(int, input().split())
        ans = n
        tmp = 0
        while n // k > 0:
            ans += n // k
            tmp = n % k
            n = n // k + tmp
        print(ans)
    except:
        break