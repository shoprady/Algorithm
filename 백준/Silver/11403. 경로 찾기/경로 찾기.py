import sys
imput = sys.stdin.readline
primt = sys.stdout.write

n = int(imput())
board = [list(map(int, imput().split())) for _ in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            if board[i][k] == board[k][j] == 1: board[i][j] = 1
for i in range(n):
    for j in range(n):
        primt(str(board[i][j]) + ' ')
    primt('\n')