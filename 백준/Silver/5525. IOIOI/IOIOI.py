n = int(input()) * 2 + 1
length = int(input())
s = list(input())

total, I_check, ls = 0, False, []
for i in range(length):
    if s[i] == 'I' and not I_check:
        I_check = True
        total += 1
        ls.append(total)
    elif s[i] == 'O' and I_check:
        I_check = False
        total += 1
        ls.append(total)
    else:
        if s[i] == 'I': total = 1
        else: total = 0
        ls.append(total)

ans = 0
for i in ls:
    if i < n: continue
    elif i >= n and i % 2 == 1: ans += 1
print(ans)