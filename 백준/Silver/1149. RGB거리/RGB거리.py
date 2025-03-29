n = int(input())
money = [list(map(int, input().split())) for _ in range(n)]
ans = [[float('inf')] * 3 for _ in range(n)]
ans[0][0], ans[0][1], ans[0][2] = money[0][0], money[0][1], money[0][2]
for i in range(1, n):
    ans[i][0] = min(ans[i - 1][1] + money[i][0], ans[i - 1][2] + money[i][0])
    ans[i][1] = min(ans[i - 1][0] + money[i][1], ans[i - 1][2] + money[i][1])
    ans[i][2] = min(ans[i - 1][0] + money[i][2], ans[i - 1][1] + money[i][2])
print(min(ans[n - 1]))