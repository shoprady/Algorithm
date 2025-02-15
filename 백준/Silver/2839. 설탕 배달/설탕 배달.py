n = int(input())
ans = n
for i in range(n // 5 + 1):
    tmp = n - 5 * i
    if tmp % 3 == 0:
        ans = min(ans, i + tmp // 3)
        
if ans == n: print(-1)
else: print(ans)