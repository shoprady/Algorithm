while True:
    n = int(input())
    if not n: break
    tmp = n
    while n > 1:
        n = 3*n+1 if n%2 else n//2
        tmp = max(n, tmp)
    print(tmp)