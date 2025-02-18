k, n = map(int, input().split())
lines = []
for _ in range(k):
    lines.append(int(input()))
    
ans, left, right = 0, 1, max(lines)
while left <= right:
    tmp = 0
    mid = (left + right) // 2
    for line in lines:
        tmp += line // mid
    
    if tmp < n:
        right = mid - 1
    else:
        left = mid + 1
        ans = max(ans, mid)
        
print(ans)