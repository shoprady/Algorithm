n, m = map(int, input().split())
mat1 = []
for _ in range(n):
    mat1.append(list(map(int, input().split())))

m, k = map(int, input().split())
mat2 = []
for _ in range(m):
    mat2.append(list(map(int, input().split())))

ans = []
for i in range(n):
    line = []
    for l in range(k):
        element = 0
        for j in range(m):
            element += mat1[i][j] * mat2[j][l]
        line.append(element)
    ans.append(line)
    
for i in range(n):
    for j in range(k):
        print(ans[i][j], end=' ')
    print()