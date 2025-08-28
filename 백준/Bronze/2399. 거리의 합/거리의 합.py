n = int(input())
ls = list(map(int, input().split()))
ans = 0
for i in ls:
    for j in ls:
        ans += abs(i-j)
print(ans)