i, j = map(int, input().split())
n, ans = i * j, []
for i in input().split():
    ans.append(int(i) - n)
for i in ans:
    print(i, end=' ')