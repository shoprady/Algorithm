from collections import deque
n, m = map(int, input().split())
board, visit = [0] * 100, [100] * 100
for _ in range(n + m):
    x, y = map(int, input().split())
    board[x - 1] = y - 1

visit[0] = 0
q = deque([0])
while q:
    now = q.popleft()
    if now == 99: break
    for i in range(1, 7):
        nxt = now + i
        if nxt > 99: break
        if board[nxt]:
            nxt = board[nxt]
        if visit[now] + 1 < visit[nxt]:
            visit[nxt] = visit[now] + 1
            q.append(nxt)
print(visit[99])