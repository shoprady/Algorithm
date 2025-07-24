n = int(input())
ls = list(map(int, input().split()))
start, tmp, ans = ls[0], ls[0], 0
for end in ls:
    ans = max(ans, end - start)
    if start > end or tmp >= end:
        start = end
    tmp = end
print(ans)