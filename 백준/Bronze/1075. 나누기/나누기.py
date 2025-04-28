n, f = int(input()), int(input())
s = f * (n // f)
if str(n)[:-2] != str(s)[:-2]:
    s += f
t = int(str(s)[-2:])
while 0 <= t < 100:
    t -= f
print('{:02d}'.format(t + f))