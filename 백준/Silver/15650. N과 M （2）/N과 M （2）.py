n, m = map(int, input().split())
ans = []
def dfs(num):
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return
    for i in range(num, n + 1):
        if i not in ans:
            ans.append(i)
            dfs(i + 1)
            ans.pop()
dfs(1)