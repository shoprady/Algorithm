n = int(input())
board = [0] * n

def check(x):
    for i in range(x):
        if board[x] == board[i]:
            return False
        if x - i == abs(board[x] - board[i]):
            return False
    return True

def queen(x):
    if x == n:
        return 1
    ans = 0
    for i in range(n):
        board[x] = i
        if check(x):
            ans += queen(x + 1)
    return ans

print(queen(0))