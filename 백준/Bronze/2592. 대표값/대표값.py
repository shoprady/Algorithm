ls = []
for _ in range(10):
    ls.append(int(input()))
print(sum(ls)//10)
d = dict()
for i in ls:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
count, ans = -1, 0
for i in d:
    if d[i] > count:
        ans, count = i, d[i]
print(ans)