n, m = map(int, input().split())
ans = []
def dfs(num):
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return
    for i in range(num, n + 1):
        ans.append(i)
        dfs(i)
        ans.pop()
dfs(1)