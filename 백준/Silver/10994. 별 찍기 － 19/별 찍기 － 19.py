n = int(input())
k = 4 * n - 3
stars = [[' '] * k for _ in range(k)]
def star(n, x, y):
    if n == 1:
        stars[x][y] = '*'; return
    k = 4 * n - 3
    for i in range(x, x + k):
        for j in range(y, y + k):
            if i == x or i == x + k - 1 or j == y or j == y + k - 1:
                stars[i][j] = '*'
    star(n - 1, x + 2, y + 2)
star(n, 0, 0)
for i in range(k):
    for j in range(k):
        print(stars[i][j], end='')
    print('')