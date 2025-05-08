n, m, l = map(int, input().split())
ls = [0] * n
i, ans = 0, 0
while True:
    ls[i] += 1
    ans += 1
    if ls[i] == m:
        break
    if ls[i] % 2:
        i += l
        if i >= n: i -= n
    else:
        i -= l
        if i < 0: i += n
print(ans - 1)