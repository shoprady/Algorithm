n = int(input())
ls = list(map(int, input().split()))
if ls[0] >= 0:
    print(ls[0], ls[1]); exit(0)
if ls[-1] <= 0:
    print(ls[-2], ls[-1]); exit(0)
ans, a, b = float('inf'), 0, 0
for p in range(n-1):
    anchor = ls[p]
    i, j = p+1, n-1
    while i <= j:
        mid = (i+j)//2
        tmp = anchor + ls[mid]
        if abs(tmp) < abs(ans):
            ans, a, b = tmp, p, mid
            if tmp == 0: break
        if tmp < 0:
            i = mid + 1
        else:
            j = mid - 1
print(ls[a], ls[b])