s, ans = input(), 0
for i in range(len(s) - 3):
    if s[i:i+4] == 'DKSH': ans += 1
print(ans)