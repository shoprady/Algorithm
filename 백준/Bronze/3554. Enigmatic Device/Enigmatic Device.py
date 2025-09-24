n, ls = int(input()), list(map(int, input().split()))
for _ in range(int(input())):
    k, l, r = map(int, input().split())
    if k == 1:
        for i in range(l-1, r):
            ls[i] = ls[i]**2 % 2010
    else:
        print(sum(ls[l-1:r]))