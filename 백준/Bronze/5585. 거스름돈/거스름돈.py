n = 1000 - int(input())
ls = [500, 100, 50, 10, 5, 1]

ans, i = 0, 0
while n > 0 and i < 6:
    if n >= ls[i]:
        n -= ls[i]
        ans += 1
    else:
        i += 1
print(ans)