n = int(input())
sx, sy, ex, ey = map(int, input().split())
dist = []
for _ in range(n):
    cx, cy, d = sx, sy, 0
    for _ in range(int(input())):
        x, y = map(int, input().split())
        d += abs(x-cx) + abs(y-cy)
        cx, cy = x, y
    d += abs(ex-cx) + abs(ey-cy)
    dist.append(d)
print(dist.index(min(dist))+1)