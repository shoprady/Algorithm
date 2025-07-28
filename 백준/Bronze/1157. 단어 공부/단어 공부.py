ls = [0] * 26
for i in list(input()):
    n = ord(i)
    if 65 <= n <= 90:
        ls[n-65] += 1
    else:
        ls[n-97] += 1
ans = max(ls)
print('?') if ls.count(ans) > 1 else print(chr(ls.index(ans)+65))