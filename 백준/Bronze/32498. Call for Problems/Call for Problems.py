n = int(input())
ans = 0
for _ in range(n):
    num = int(input())
    if num % 2 != 0: ans += 1
print(ans)