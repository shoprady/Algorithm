i = int(input())
x = i
check = False
while x < 9999:
    x += 1
    a, b = int(str(x)[:2]), int(str(x)[2:])
    if (a+b)**2 == x:
        check = True
        break
if check:
    ans = int(str(a)+str(b).zfill(2))
    print(ans)
else: print(-1)