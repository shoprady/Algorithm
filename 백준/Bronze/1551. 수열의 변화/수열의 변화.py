n, k = map(int, input().split())
ls = list(map(int, input().split(',')))
for l in range(k):
    if l > 0: ls = ans
    ans = []
    for i in range(n-1-l):
        ans.append(ls[i+1] - ls[i])
for i in range(n-k):
    if k == 0:
        ans = ls
    print(ans[i], end=',') if i < n-k-1 else print(ans[i])