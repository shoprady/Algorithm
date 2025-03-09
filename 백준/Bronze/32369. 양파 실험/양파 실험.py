n, a, b = map(int, input().split())
good, bad = 1, 1
for _ in range(n):
    good += a; bad += b
    if good > bad: continue
    elif good < bad: good, bad = bad, good
    else: bad -= 1
print(good, bad)