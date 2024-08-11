n, k = map(int, input().split())
ans = 0
if k >= 0 and k <= n:
    a1, a2 = 1, 1
    for i in range(k+1, n+1):
        a1 *= i
    for i in range(1, n-k+1):
        a2 *= i
    ans = int(a1 / a2)
print(ans)