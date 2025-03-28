n, m = map(int, input().split())
arr = [[float('inf')] * n for _ in range(n)]
for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    arr[a][b] = arr[b][a] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

bacon = []
for i in range(n):
    bacon.append(sum(arr[i]) - arr[i][i])
print(bacon.index(min(bacon)) + 1)