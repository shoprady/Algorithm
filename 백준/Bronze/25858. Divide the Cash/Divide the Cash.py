n, d = map(int, input().split())
ls = []
for _ in range(n):
    ls.append(int(input()))
i = d // sum(ls)
for j in ls:
    print(i * j)