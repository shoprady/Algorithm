import math

def z(x, y, n, init):
    global ans
    order, per = 0, 4 ** (int(math.log(n, 2)) - 1)
    for i in range(x, x + n // 2 + 1, n // 2):
        for j in range(y, y + n // 2 + 1, n // 2):
            ans = order * per + init; order += 1
            if i == r and j == c: return
    if n == 2: return
    elif x <= r < x + n // 2 and y <= c < y + n // 2:
        z(x, y, n // 2, init)
    elif x <= r < x + n // 2 and y + n // 2 <= c < y + n:
        z(x, y + n // 2, n // 2, init + per)
    elif x + n // 2 <= r < x + n and y <= c < y + n // 2:
        z(x + n // 2, y, n // 2, init + per * 2)
    else: z(x + n // 2, y + n // 2, n // 2, init + per * 3)

n, r, c = map(int, input().split())
z(0, 0, 2 ** n, 0)
print(ans)