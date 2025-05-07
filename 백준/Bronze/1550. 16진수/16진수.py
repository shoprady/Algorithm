s = input()[::-1]
ans, k = 0, 0
for i in s:
    if i.isalpha():
        ans += (ord(i) - 55) * 16 ** k
    else:
        ans += int(i) * 16 ** k
    k += 1
print(ans)