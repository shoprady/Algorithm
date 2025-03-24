n = 4 * int(input()) - 3
stars = [[' '] * n for _ in range(n)]
def star(n, x, y):
    if n == 1:
        stars[x][y] = '*'; return
    for i in range(x, x + n):
        for j in range(y, y + n):
            if i == x or i == x + n - 1 or j == y or j == y + n - 1:
                stars[i][j] = '*'
    star(n - 4, x + 2, y + 2)
star(n, 0, 0)
for i in range(n):
    for j in range(n):
        print(stars[i][j], end='')
    print('')