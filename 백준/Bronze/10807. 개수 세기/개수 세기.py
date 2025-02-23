n = int(input())
ls = list(map(int, input().split()))
v = int(input())
ans = 0
for i in ls:
    if i == v: ans += 1
print(ans)