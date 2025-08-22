n = int(input())
i = 1
ans, ans_ls = 0, []
while i <= n:
    tmp = 2
    ls = [n, i]
    nn, ii = n, i
    while True:
        nn -= ii
        if nn >= 0:
            ls.append(nn)
            tmp += 1
        else: break
        ii -= nn
        if ii >= 0:
            ls.append(ii)
            tmp += 1
        else: break
    if tmp > ans:
        ans = tmp
        ans_ls = ls
    i += 1
print(ans)
for i in ans_ls:
    print(i, end=' ')