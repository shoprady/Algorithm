import sys
print = sys.stdout.write

def square(n, x, y):
    if n == 3:
        for i in range(x, x + 3):
            for j in range(y, y + 3):
                if i == x + 1 and j == y + 1: continue
                board[i][j] = '*'
        return
    k = n // 3
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1: continue
            square(k, x + k * i, y + k * j)

n = int(input())
board = [[' '] * n for _ in range(n)]
square(n, 0, 0)
for i in range(n):
    for j in range(n):
        print(board[i][j])
    print('\n')