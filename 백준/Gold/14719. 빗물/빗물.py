h, w = map(int, input().split())
field = [[0 for j in range(w)] for i in range(h)]

heights = list(map(int, input().split()))

# 필드 구현
for i in range(w):
    height = heights[i]
    if height == 0:
        continue
    for j in range(h - 1, -1, -1):
        field[j][i] = 1
        height -= 1
        if height == 0:
            break

# 빗물의 합 계산
sum = 0
for i in range(h):
    for j in range(w):
        if field[i][j] == 1:
            temp = 0
            for k in range(j + 1, w):
                if field[i][k] == 1:
                    sum += temp
                    break
                temp += 1
            
print(sum)