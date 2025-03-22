n, m = map(int, input().split())
ls, ans, result = sorted(list(map(int, input().split()))), [], set()
def dfs(num):
    if len(ans) == m:
        tmp = ' '.join(map(lambda x: str(ls[x]), ans))
        if tmp not in result:
            print(tmp); result.add(tmp)
        return
    for i in range(num, n):
        ans.append(i)
        dfs(i)
        ans.pop()
dfs(0)