n, k = map(int, input().split())
ls = []
for _ in range(n):
    ls.append(list(map(int, input().split())))
col = [list(c) for c in zip(*ls)]

ans = float('inf')
ls.sort(key=lambda x: x[2])
for a in col[0]:
    for b in col[1]:
        c, cnt = 0, 0
        for i in range(n):
            if ls[i][0] <= a and ls[i][1] <= b:
                c = max(c, ls[i][2])
                cnt += 1
            if cnt == k: break
        if cnt == k: ans = min(ans, a+b+c)
print(ans)