n, c = map(int, input().split())
x = y = z = 0
for _ in range(n):
    a, t = input().split()
    x += int(a)
    if t == 'bedroom':
        y += int(a)
    if t == 'balcony':
        z += int(a) / 2
    else:
        z += int(a)
print(x)
print(y)
print(z * c)