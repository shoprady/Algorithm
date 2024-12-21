n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
cnt0, cnt1 = 0, 0

def check_paper(x, y, n):
    global cnt0, cnt1
    flag = True
    
    for i in range(x, x + n):
        for j in range(y + 1, y + n):
            if i == x:
                if paper[i][j] != paper[i][j - 1]:
                    check_paper(x, y, n // 2)
                    check_paper(x + n // 2, y, n // 2)
                    check_paper(x, y + n // 2, n // 2)
                    check_paper(x + n // 2, y + n // 2, n // 2)
                    flag = False; return
            else:
                if paper[i][j] != paper[i - 1][j] or paper[i][j] != paper[i][j - 1]:
                    check_paper(x, y, n // 2)
                    check_paper(x + n // 2, y, n // 2)
                    check_paper(x, y + n // 2, n // 2)
                    check_paper(x + n // 2, y + n // 2, n // 2)
                    flag = False; return
                
    if flag:
        if paper[x][y] == 0: cnt0 += 1
        else: cnt1 += 1

            
check_paper(0, 0, n)
print(cnt0)
print(cnt1)