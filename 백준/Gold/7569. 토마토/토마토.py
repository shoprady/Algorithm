from collections import deque
dx, dy, dz = [-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1]

def make_tomato():
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx, ny, nz = dx[i] + x, dy[i] + y, dz[i] + z
            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and box[nx][ny][nz] == 0:
                box[nx][ny][nz] = box[x][y][z] + 1
                queue.append((nx, ny, nz))

def check_all():
    check = True
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if box[i][j][k] == 0:
                    check = False; break
    return check
    
if __name__ == "__main__":
    m, n, h = map(int, input().split())
    box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
    queue = deque()
    
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if box[i][j][k] == 1:
                    queue.append((i, j, k))
    
    make_tomato()
    time = max(num for sublist in box for inner_list in sublist for num in inner_list)
    if check_all(): print(time - 1)
    else: print(-1)