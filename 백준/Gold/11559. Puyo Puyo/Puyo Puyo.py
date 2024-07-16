# 상하좌우 탐색 시 사용
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 주변에서 같은 뿌요 탐색 (BFS)
def search_puyo(x, y):
    same_puyos = []
    queue = [(x, y)]
    
    while queue:
        x, y = queue.pop(0)
        
        # 상하좌우 탐색
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            
            if nx == -1 or nx == 12 or ny == -1 or ny == 6:
                continue
                
            elif board[x][y] == board[nx][ny] and (nx, ny) not in same_puyos:
                same_puyos.append((nx, ny))
                queue.append((nx, ny))
                
    return same_puyos


# 뿌요 터뜨리기
def puyo_pop(same_puyos):
    for x, y in same_puyos:
        board[x][y] = '.'
    
    
# 뿌요 내리기
def puyo_down():
    for y in range(6):
        queue = []
        for x in range(11, -1, -1):
            if board[x][y] != '.':
                queue.append(board[x][y])
                board[x][y] = '.'
        for x in range(11, -1, -1):
            if queue:
                board[x][y] = queue.pop(0)
            else:
                break

        
if __name__ == "__main__":
    board = [list(input()) for _ in range(12)]
    combo = 0 # 연쇄 수
    
    while True:
        check = False
        
        for x in range(12):
            for y in range(6):
                if board[x][y] != '.':
                    same_puyos = search_puyo(x, y)
                    if len(same_puyos) >= 4:
                        puyo_pop(same_puyos)
                        check = True
        
        if check == True:
            puyo_down()
            combo += 1
        else:
            break
                    
    print(combo)