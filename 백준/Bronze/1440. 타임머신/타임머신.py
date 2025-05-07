ls = list(map(int, input().split(':')))
ans = 6
for i in ls:
    if i > 59:
        ans = 0
        break
    elif i == 0 or i > 12:
        ans -= 2
print(ans)