k, n = map(int, input().split())
budgets = []
for _ in range(k):
    budgets.append(int(input()))
    
ans, left, right = 0, 1, max(budgets)
while left <= right:
    tmp = 0
    mid = (left + right) // 2
    for budget in budgets:
        tmp += budget // mid
    
    if tmp < n:
        right = mid - 1
    else:
        left = mid + 1
        ans = max(ans, mid)
        
print(ans)