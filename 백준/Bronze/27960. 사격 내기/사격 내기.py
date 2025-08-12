a, b = map(int, input().split())
al, bl = [], []
for i in range(9, -1, -1):
    if a >= 2 ** i:
        a -= 2 ** i
        al.append(i)
    if b >= 2 ** i:
        b -= 2 ** i
        bl.append(i)
ans = 0
for i in range(9, -1, -1):
    if i in al and i in bl:
        continue
    elif i not in al and i not in bl:
        continue
    else:
        ans += 2 ** i
print(ans)