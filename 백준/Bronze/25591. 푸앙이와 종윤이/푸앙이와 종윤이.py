m, n = map(int, input().split())
a, b = 100 - m, 100 - n
c, d = 100 - (a + b), a * b
q, r = d // 100, d % 100
print(a, b, c, d, q, r)
print(c, d) if d < 100 else print(c + q, r)