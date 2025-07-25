ls, tmp, ans = [], 0, 0
for _ in range(int(input())):
    ls.append(int(input()))
for i in range(-1, -len(ls)-1, -1):
    if ls[i] > tmp:
        ans += 1
    tmp = max(tmp, ls[i])
print(ans)