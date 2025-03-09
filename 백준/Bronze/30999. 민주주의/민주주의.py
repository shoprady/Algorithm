n, m = map(int, input().split())
ans = 0
for _ in range(n):
    s = list(input())
    if s.count('O') > len(s) // 2: ans += 1
print(ans)