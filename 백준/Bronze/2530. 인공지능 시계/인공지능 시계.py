h, m, s = map(int, input().split())
sec = int(input())
if sec < 3600:
    m += sec // 60; s += sec % 60
else:
    h += sec // 3600
    sec -= 3600 * (sec // 3600)
    m += sec // 60; s += sec % 60
    
if s >= 60:
    m += s // 60; s -= 60 * (s // 60)
if m >= 60:
    h += m // 60; m -= 60 * (m // 60)
if h >= 24:
    h -= 24 * (h // 24)
print(h, m, s)