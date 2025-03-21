n, m = map(int, input().split())
ls, ans = sorted(list(map(int, input().split()))), []
def dfs():
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return
    for i in range(n):
        if ls[i] not in ans:
            ans.append(ls[i])
            dfs()
            ans.pop()
dfs()