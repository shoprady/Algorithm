k = int(input())
if k == 1: print('*'); exit(0)
n, m = 4 * k - 3, 4 * k - 1
stars = [[' '] * n for _ in range(m)]
def star(n, m, x, y):
    if n == 1:
        for i in range(x, x + 3):
            stars[i][y] = '*'
        return
    for i in range(x, x + m):
        stars[i][y] = '*'
        stars[i][y + n - 1] = '*'
    for i in range(y, y + n):
        stars[x][i] = '*'
        stars[x + m - 1][i] = '*'
    stars[x + 1][y + n - 1] = ' '
    stars[x + 2][y + n - 2] = '*'
    star(n - 4, m - 4, x + 2, y + 2)
star(n, m, 0, 0)
for i in range(m):
    for j in range(n):
        print(stars[i][j], end='')
        if i == 1: break
    print('')