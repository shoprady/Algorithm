st = 'SciComLove'
s = input()
ans = 0
for i in range(10):
    if s[i] != st[i]:
        ans += 1
print(ans)