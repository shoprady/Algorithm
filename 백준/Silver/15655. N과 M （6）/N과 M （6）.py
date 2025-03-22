n, m = map(int, input().split())
ls, ans = sorted(list(map(int, input().split()))), []
def dfs(num):
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return
    for i in range(num, len(ls)):
        if ls[i] not in ans:
            ans.append(ls[i])
            dfs(i + 1)
            ans.pop()
dfs(0)