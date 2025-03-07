from collections import deque
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def update(i, j):
    ans, q = 0, deque([(i, j)])
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if nx == -1 or nx == n or ny == -1 or ny == m \
               or board[nx][ny] == 'X' or board[nx][ny] == 'I':
                continue
            elif board[nx][ny] == 'P':
                ans += 1
            board[nx][ny] = 'I'
            q.append((nx, ny))
    return ans

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(input()))
for i in range(n):
    for j in range(m):
        if board[i][j] == 'I':
            n = update(i, j)
            if n == 0: print('TT')
            else: print(n)
            exit(0)