import sys
input = sys.stdin.readline
def print(s):
    sys.stdout.write(str(s) + '\n')

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == 0 and j == 0: continue
        elif i == 0: board[i][j] += board[i][j - 1]
        elif j == 0: board[i][j] += board[i - 1][j]
        else: board[i][j] += board[i - 1][j] + board[i][j - 1] - board[i - 1][j - 1]

for _ in range(m):
    x1, y1, x2, y2 = map(lambda x: int(x) - 1, input().split())
    if x1 == 0 and y1 == 0: print(board[x2][y2])
    elif x1 == 0: print(board[x2][y2] - board[x2][y1 - 1])
    elif y1 == 0: print(board[x2][y2] - board[x1 - 1][y2])
    else: print(board[x2][y2] - board[x2][y1 - 1] - board[x1 - 1][y2] + board[x1 - 1][y1 - 1])