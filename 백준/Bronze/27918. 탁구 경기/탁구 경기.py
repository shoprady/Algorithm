d, p = 0, 0
for _ in range(int(input())):
    if input() == 'D': d += 1
    else: p += 1
    if d == p + 2 or p == d + 2: break
print('{0}:{1}'.format(d, p))