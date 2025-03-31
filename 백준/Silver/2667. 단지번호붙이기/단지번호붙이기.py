from collections import deque
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
q = deque([])

def bfs(i, j):
    q.append((i, j))
    board[i][j] = 2
    count = 0
    while q:
        x, y = q.popleft()
        count += 1
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 1:
                q.append((nx, ny))
                board[nx][ny] = 2
    return count

n = int(input())
board = [list(map(int, list(input()))) for _ in range(n)]
ans = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            ans.append(bfs(i, j))
ans.sort()
print(len(ans))
for i in ans:
    print(i)