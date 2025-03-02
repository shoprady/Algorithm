import sys
from collections import deque
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs():
    ans, visited = 0, [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                queue = deque([(i, j)])
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < n and 0 <= ny < n:
                            if board[x][y] == board[nx][ny] and not visited[nx][ny]:
                                queue.append((nx, ny)); visited[nx][ny] = 1
                ans += 1
    return ans

n = int(input())
board = []
for _ in range(n):
    board.append(list(sys.stdin.readline()))
    
ans_1 = bfs()
for i in range(n):
    for j in range(n):
        if board[i][j] == 'R': board[i][j] = 'G'
ans_2 = bfs()
print(ans_1, ans_2)