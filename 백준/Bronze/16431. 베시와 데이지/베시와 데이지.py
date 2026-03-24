ls, b, d = [], 0, 0
for _ in range(3):
    ls.extend(list(map(int, input().split())))

while ls[0]!=ls[4] or ls[1]!=ls[5]:
    b += 1
    if ls[0] > ls[4]: ls[0] -= 1
    elif ls[0] < ls[4]: ls[0] += 1
    if ls[1] > ls[5]: ls[1] -= 1
    elif ls[1] < ls[5]: ls[1] += 1

while ls[2]!=ls[4] or ls[3]!=ls[5]:
    d += 1
    if ls[2] > ls[4]: ls[2] -= 1
    elif ls[2] < ls[4]: ls[2] += 1
    elif ls[3] > ls[5]: ls[3] -= 1
    elif ls[3] < ls[5]: ls[3] += 1

if b > d: print('daisy')
elif b < d: print('bessie')
else: print('tie')