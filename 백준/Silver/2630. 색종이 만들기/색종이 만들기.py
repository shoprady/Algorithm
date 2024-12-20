n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
cnt0, cnt1 = 0, 0

def check_paper(x, y, n):
    global cnt0, cnt1
    tmp = 0
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] == 0: tmp += 1
    if tmp == n * n: cnt0 += 1
    elif tmp == 0: cnt1 += 1
    else:
        check_paper(x, y, n // 2)
        check_paper(x + n // 2, y, n // 2)
        check_paper(x, y + n // 2, n // 2)
        check_paper(x + n // 2, y + n // 2, n // 2)

check_paper(0, 0, n)
print(cnt0)
print(cnt1)