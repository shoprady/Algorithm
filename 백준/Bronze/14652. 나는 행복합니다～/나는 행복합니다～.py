n, m, k = map(int, input().split())
for i in range(n):
    for j in range(m):
        if i * m + j == k: print(i, j)