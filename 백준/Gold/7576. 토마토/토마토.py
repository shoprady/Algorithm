from collections import deque
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def make_tomato():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                queue.append((nx, ny))

def check_all():
    check = True
    for i in range(n):
        for j in range(m):
            if box[i][j] == 0:
                check = False; break
    return check
    
if __name__ == "__main__":
    m, n = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(n)]
    queue = deque()
    
    for i in range(n):
        for j in range(m):
            if box[i][j] == 1:
                queue.append((i, j))
    
    make_tomato()
    if check_all(): print(max(map(max, box)) - 1)
    else: print(-1)