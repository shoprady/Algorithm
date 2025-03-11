n, x = map(int, input().split())
ls = list(map(int, input().split()))
ans = float("inf")
for i in range(1, n):
    ans = min(ls[i - 1] + ls[i], ans)
print(x * ans)