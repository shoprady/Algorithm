n, times = int(input()), list(map(int, input().split()))
y, m = 0, 0
for i in times:
    y += (i // 30 + 1) * 10
    m += (i // 60 + 1) * 15
if y < m: print('Y', y)
elif m < y: print('M', m)
else: print('Y', 'M', y)