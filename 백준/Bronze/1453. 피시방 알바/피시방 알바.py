n, ls = int(input()), [0] * 100
ans = 0
for i in map(int, input().split()):
    if ls[i-1]:
        ans += 1
    else:
        ls[i-1] = 1
print(ans)