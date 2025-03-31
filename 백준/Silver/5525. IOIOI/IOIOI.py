n = int(input()) * 2 + 1
length = int(input())
s = input()

p = ''
for i in range(n):
    if i % 2 == 0: p += 'I'
    else: p += 'O'

ans = 0
for i in range(length - n + 1):
    if s[i:i+n] == p: ans += 1
print(ans)