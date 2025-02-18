n, m = map(int, input().split())
trees = list(map(int, input().split()))
    
ans, left, right = 0, 1, max(trees)
while left <= right:
    tmp = 0
    mid = (left + right) // 2
    for tree in trees:
        if tree > mid:
            tmp += tree - mid
            
    if tmp < m:
        right = mid - 1
    else:
        left = mid + 1
        ans = max(ans, mid)
        
print(ans)