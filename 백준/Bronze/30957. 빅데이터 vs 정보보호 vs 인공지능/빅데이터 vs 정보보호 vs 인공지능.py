n = int(input())
b, s, a = 0, 0, 0
for i in input():
    if i == 'B': b += 1
    elif i == 'S': s += 1
    else: a += 1

ans = ''
m = max(b,s,a)
if b == m: ans += 'B'
if s == m: ans += 'S'
if a == m: ans += 'A'

print('SCU') if ans == 'BSA' else print(ans)