import sys
n, m, b = map(int, input().split())
gr = []
for _ in range(n):
    gr.extend(list(map(int, sys.stdin.readline().split())))
time, height = float('inf'), 0
for h in range(257):
    t, inv = 0, b
    for i in range(n * m):
        diff = gr[i] - h
        if diff > 0: t += diff * 2
        elif diff < 0: t += -diff
        inv += diff
    if inv >= 0 and min(time, t) == t: time, height = t, h
print(time, height)