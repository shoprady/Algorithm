a, b, n = map(int, input().split())
a -= b * (a//b)
a *= 10
for _ in range(n):
    ans = a//b
    a -= b * ans
    a *= 10
print(ans)