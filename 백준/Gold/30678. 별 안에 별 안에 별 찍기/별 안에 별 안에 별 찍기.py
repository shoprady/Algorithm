import sys
print = sys.stdout.write

def star(n, x, y):
    if n == 1:
        board[x][y] = '*'; return
    k = n // 5
    for i in range(2):
        star(k, x+k*i, y)
    for i in range(y-2*k, y+2*k+1, k):
        star(k, x+2*k, i)
    for i in range(y-k, y+k+1, k):
        star(k, x+3*k, i)
    star(k, x+4*k, y-k); star(k, x+4*k, y+k)

n = int(input())
k = 5 ** n
board = [[' '] * k for _ in range(k)]
star(k, 0, k // 2)
for i in range(k):
    for j in range(k):
        print(board[i][j])
    print('\n')