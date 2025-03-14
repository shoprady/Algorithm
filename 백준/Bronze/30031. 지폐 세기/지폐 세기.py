ans = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a == 136: ans += 1000
    elif a == 142: ans += 5000
    elif a == 148: ans += 10000
    else: ans += 50000
print(ans)