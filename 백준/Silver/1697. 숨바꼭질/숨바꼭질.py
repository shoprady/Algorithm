from collections import deque
n, k = map(int, input().split())
if n == k: print(0); exit(0)
visit = [0] * 100001
q = deque([n])
while q:
    x = q.popleft()
    if x > 0 and not visit[x - 1]:
        visit[x - 1] = visit[x] + 1
        q.append(x - 1)
    if x < 100000 and not visit[x + 1]:
        visit[x + 1] = visit[x] + 1
        q.append(x + 1)
    if x < 50001 and not visit[x * 2]:
        visit[x * 2] = visit[x] + 1
        q.append(x * 2)
print(visit[k])