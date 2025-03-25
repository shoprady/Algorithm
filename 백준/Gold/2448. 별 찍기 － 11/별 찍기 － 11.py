import sys
print = sys.stdout.write

def triangle(n, x, y):
    if n == 3:
        board[x][y] = board[x+1][y-1] = board[x+1][y+1] = '*'
        for i in range(y - 2, y + 3):
            board[x+2][i] = '*'
        return
    k = n // 2
    triangle(k, x, y)
    triangle(k, x+k, y-k)
    triangle(k, x+k, y+k)

n = int(input())
board = [[' '] * (n * 2) for _ in range(n)]
triangle(n, 0, n-1)
for i in range(n):
    for j in range(n * 2):
        print(board[i][j])
    print('\n')