import sys
from collections import deque
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(i, j):
    q = deque([(i, j)])
    while q:
        x, y = q.popleft()
        visit[x][y] = 1
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny] and board[nx][ny]:
                board[nx][ny] = board[x][y] + 1
                visit[nx][ny] = 1; q.append((nx, ny))

def pr():
    for i in range(n):
        for j in range(m):
            if board[i][j]: print(board[i][j] - 2, end=' ')
            else: print(board[i][j], end=' ')
        print('')

n, m = map(int, input().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visit = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            bfs(i, j); pr(); exit(0)