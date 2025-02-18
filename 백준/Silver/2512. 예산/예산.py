n = int(input())
budgets = list(map(int, input().split()))
m = int(input())
    
ans, left, right = 0, 1, max(budgets)
while left <= right:
    tmp = 0
    mid = (left + right) // 2
    for budget in budgets:
        tmp += min(budget, mid)
            
    if tmp > m:
        right = mid - 1
    else:
        left = mid + 1
        ans = max(ans, mid)
        
print(ans)