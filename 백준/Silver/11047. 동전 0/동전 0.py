n, k = map(int, input().split())
val, ans = [], 0
for _ in range(n):
    val.append(int(input()))
    
for i in range(n - 1, -1, -1):
    if val[i] > k:
        continue
    tmp = k // val[i]
    k -= tmp * val[i]
    ans += tmp
    
print(ans)