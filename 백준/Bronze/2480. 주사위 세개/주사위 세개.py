ls = list(map(int, input().split()))
ans = 0
for i in range(1, 7):
    if ls.count(i) == 2:
        ans = 1000 + i * 100; break
    elif ls.count(i) == 3:
        ans = 10000 + i * 1000; break
if ans: print(ans)
else: print(max(ls) * 100)