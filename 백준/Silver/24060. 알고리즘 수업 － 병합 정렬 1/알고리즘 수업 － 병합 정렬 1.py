def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    i, j, tmp = p, q + 1, []
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1
            
    while i <= q: # 왼쪽 배열 남음
        tmp.append(A[i])
        i += 1
    while j <= r: # 오른쪽 배열 남음
        tmp.append(A[j])
        j += 1
        
    i = p
    for t in tmp:
        A[i] = t
        ans.append(t)
        i += 1

n, k = map(int, input().split())
A = list(map(int, input().split()))

ans = []
merge_sort(A, 0, n - 1)
print(ans[k - 1] if len(ans) >= k else -1)