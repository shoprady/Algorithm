s = input()
ans = ''
for c in s:
    asc = ord(c)
    if asc < 91: ans += chr(asc + 32)
    else: ans += chr(asc - 32)
print(ans)