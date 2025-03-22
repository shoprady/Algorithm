n, m = map(int, input().split())
ls, ans, result = sorted(list(map(int, input().split()))), [], []
def dfs(num):
    if len(ans) == m:
        tmp = ' '.join(map(lambda x: str(ls[x]), ans))
        if tmp not in result:
            print(tmp); result.append(tmp)
    for i in range(num, n):
        if i not in ans:
            ans.append(i)
            dfs(i + 1)
            ans.pop()
dfs(0)