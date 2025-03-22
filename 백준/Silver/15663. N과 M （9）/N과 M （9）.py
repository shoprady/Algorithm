n, m = map(int, input().split())
ls, ans, result = sorted(list(map(int, input().split()))), [], []
def dfs():
    if len(ans) == m:
        tmp = ' '.join(map(lambda x: str(ls[x]), ans))
        if tmp not in result:
            print(tmp); result.append(tmp)
        return
    for i in range(n):
        if i not in ans:
            ans.append(i)
            dfs()
            ans.pop()
dfs()