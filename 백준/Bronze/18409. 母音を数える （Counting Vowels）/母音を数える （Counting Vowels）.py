n, s, ans = int(input()), input(), 0
dic = {'a':0, 'i':0, 'u':0, 'e':0, 'o':0}
for i in s:
    if i in dic: ans += 1
print(ans)