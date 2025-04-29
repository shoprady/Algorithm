board = [list(input()) for _ in range(8)]
odd_check, ans = False, 0
for i in range(8):
    if odd_check:
        for j in range(1, 8, 2):
            if board[i][j] == 'F': ans += 1
    else:
        for j in range(0, 8, 2):
            if board[i][j] == 'F': ans += 1
    odd_check = False if odd_check else True
print(ans)