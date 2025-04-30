N, m, M, T, R = map(int, input().split())
ans, ex, X, check = 0, 0, m, True
while ex < N:
    if X + T <= M:
        X += T
        ex += 1
    elif X - R > m:
        X -= R
    elif ex == 0:
        ans = -1; break
    else:
        X = m
    ans += 1
print(ans)