board, ans = [list(input()) for _ in range(8)], 0
for i in range(8):
    for j in range(8):
        if board[i][j] == 'K': continue
        elif board[i][j] == 'P': ans += 1
        elif board[i][j] == 'N': ans += 3
        elif board[i][j] == 'B': ans += 3
        elif board[i][j] == 'R': ans += 5
        elif board[i][j] == 'Q': ans += 9
        elif board[i][j] == 'k': continue
        elif board[i][j] == 'p': ans -= 1
        elif board[i][j] == 'n': ans -= 3
        elif board[i][j] == 'b': ans -= 3
        elif board[i][j] == 'r': ans -= 5
        elif board[i][j] == 'q': ans -= 9
print(ans)