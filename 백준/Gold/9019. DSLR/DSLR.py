from collections import deque

def d(n):
    return (n * 2) % 10000

def s(n):
    if n == 0:
        return 9999
    else:
        return n - 1

def l(n):
    return (n % 1000) * 10 + n // 1000

def r(n):
    return (n % 10) * 1000 + n // 10

for _ in range(int(input())):
    a, b = map(int, input().split())
    visited = [False] * 10000
    q = deque([(a, "")])
    while q:
        n, ans = q.popleft()
        if n == b:
            print(ans)
            break
        for i, j in [(d(n), 'D'), (s(n), 'S'), (l(n), 'L'), (r(n), 'R')]:
            if not visited[i]:
                visited[i] = True
                q.append((i, ans + j))