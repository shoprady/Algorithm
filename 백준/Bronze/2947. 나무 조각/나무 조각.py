a, b, c, d, e = map(int, input().split())
while True:
    if a > b:
        a, b = b, a
        print(a, b, c, d, e)
    if b > c:
        b, c = c, b
        print(a, b, c, d, e)
    if c > d:
        c, d = d, c
        print(a, b, c, d, e)
    if d > e:
        d, e = e, d
        print(a, b, c, d, e)
    if a < b < c < d < e:
        break