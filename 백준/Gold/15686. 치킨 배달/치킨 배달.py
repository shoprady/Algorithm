n, m = map(int, input().split())
ls, chick = [], []
for _ in range(n):
    ls.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        if ls[i][j] == 2: chick.append((i, j))

def compute(i, j, selected):
    ans = []
    for a, b in selected:
        ans.append(abs(i-a) + abs(j-b))
    return min(ans)

def compute_all(selected):
    ans = 0
    for i in range(n):
        for j in range(n):
            if ls[i][j] == 1:
                ans += compute(i, j, selected)
    return ans

def chick_backtrack():
    def backtrack(start, selected):
        if len(selected) == m:
            result.append(compute_all(selected))
            return
        for i in range(start, len(chick)):
            selected.append(chick[i])
            backtrack(i+1, selected)
            selected.pop()
    result = []
    backtrack(0, [])
    return min(result)

if len(chick) == m:
    print(compute_all(chick))
else:
    print(chick_backtrack())