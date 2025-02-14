def check_board(check):
    min_diff, diff = 64, 64
    for start1 in range(n - 7):
        for start2 in range(m - 7):
            min_diff, diff = min(min_diff, diff), 0
            for i in range(start1, start1 + 8):
                for j in range(start2, start2 + 8):
                    if board[i][j] != check[j - start2]:
                        diff += 1
                if check == bw: check = wb
                else: check = bw
    return min(min_diff, diff)

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(input())

bw = 'BWBWBWBW'
wb = 'WBWBWBWB'

diff_bw, diff_wb = check_board(bw), check_board(wb)
print(min(diff_bw, diff_wb))