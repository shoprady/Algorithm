arr = [[0] * 100 for _ in range(100)]
for _ in range(4):
    ax, ay, bx, by = map(int, input().split())
    for i in range(ay, by):
        for j in range(ax, bx):
            arr[i][j] = 1
print(sum(sum(row) for row in arr))