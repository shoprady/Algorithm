ans = 1001
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a <= b: ans = min(ans, b)
    else: continue
print(-1) if ans == 1001 else print(ans)