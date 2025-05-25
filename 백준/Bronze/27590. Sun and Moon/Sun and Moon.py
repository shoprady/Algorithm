a, b = map(int, input().split())
c, d = map(int, input().split())
x, y = b - a, d - c
while x != y:
    if x > y: y += d
    else: x += b
print(x)