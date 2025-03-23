ans = 0
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if a == b == c:
        total = 10000 + 1000 * a
    elif a == b or a == c:
        total = 1000 + 100 * a
    elif b == c:
        total = 1000 + 100 * b
    else: total = 100 * max(a, b, c)
    ans = max(total, ans)
print(ans)