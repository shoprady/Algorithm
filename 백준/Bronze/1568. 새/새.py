n = int(input())
i, ans = 1, 0
while n > 0:
    if i > n:
        i = 1
    n -= i
    i += 1
    ans += 1
print(ans)