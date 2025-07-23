s = list(input())
ch = 0
ans = 0
for i in range(13):
    if s[i] == '*':
        ch = i
    elif i % 2 == 0:
        ans += int(s[i])
    else:
        ans += int(s[i]) * 3
if ans % 10 == 0:
    print(0)
elif ch % 2 == 0:
    print(10 - ans % 10)
else:
    a = 10 - ans % 10
    while a % 3:
        a += 10
    print(a // 3)