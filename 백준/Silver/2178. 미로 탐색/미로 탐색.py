from collections import deque
n, m = map(int, input().split())
board = [list(map(int, list(input()))) for _ in range(n)]
visit = [[0] * m for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

q, ans = deque([(0, 0)]), float('inf')
visit[0][0] = 1
while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and \
           board[nx][ny] and not visit[nx][ny]:
            q.append((nx, ny))
            visit[nx][ny] = visit[x][y] + 1
        if nx == n - 1 and ny == m - 1:
            ans = min(ans, visit[nx][ny])
print(ans)