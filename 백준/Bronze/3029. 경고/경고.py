h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))
h, m, s = h2-h1, m2-m1, s2-s1
if h == m == s: h = 24
if s < 0:
    s += 60
    m -= 1
if m < 0:
    m += 60
    h -= 1
if h < 0:
    h += 24
print('{0:02d}:{1:02d}:{2:02d}'.format(h, m, s))