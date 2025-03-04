a, b = map(int, input().split())
x, y = -1, -1
for i in range(0, 1000):
    j = a - i
    if 0 <= j <= 1000 and abs(i - j) == b:
        x, y = i, j; break
if x == -1: print(-1)
else: print(max(x, y), min(x, y))