# 상하좌우 검사
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def BFS(x, y):
    if field[x][y] == -1: # already checked
        return
    
    global ans
    ans += 1
    queue = [(x, y)]
    field[x][y] = -1 # checked
    
    while queue:
        a, b = queue.pop(0)
        for i in range(4):
            na, nb = a+dx[i], b+dy[i]
            if na < 0 or na >= n or nb < 0 or nb >= m:
                continue
            if field[na][nb] == 1:
                queue.append((na, nb))
                field[na][nb] = -1 # checked

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    field, points = [[0 for _ in range(m)] for _ in range(n)], []
    for _ in range(k):
        b, a = map(int, input().split())
        field[a][b] = 1
        points.append((a, b))
        
    ans = 0
    for point in points:
        x, y = point
        BFS(x, y)
    print(ans)