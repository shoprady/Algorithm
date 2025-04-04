x, y = map(int, input().split())
ans = x / y * 1000
for _ in range(int(input())):
    x, y = map(int, input().split())
    ans = min(ans, x / y * 1000)
print('{:.2f}'.format(ans))