no = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
s = input().split()
ans = ''
for i in range(len(s)):
    if s[i] not in no:
        ans += s[i][0].upper()
    elif i == 0:
        ans += s[i][0].upper()
print(ans)