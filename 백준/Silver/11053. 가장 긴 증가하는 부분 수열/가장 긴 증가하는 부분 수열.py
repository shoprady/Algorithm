n = int(input())
arr = list(map(int, input().split()))
ans = [0] * n
for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            ans[i] = max(ans[i], ans[j] + 1)
print(max(ans) + 1)