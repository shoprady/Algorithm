def merge_sort(A, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid + 1, right)
        merge(A, left, mid, right)

def merge(A, left, mid, right):
    i, j, tmp = left, mid + 1, []
    while i <= mid and j <= right:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1
            
    while i <= mid: # 왼쪽 배열 남음
        tmp.append(A[i])
        i += 1
    while j <= right: # 오른쪽 배열 남음
        tmp.append(A[j])
        j += 1
        
    i = left
    for t in tmp:
        A[i] = t
        ans.append(t)
        i += 1

n, k = map(int, input().split())
A = list(map(int, input().split()))

ans = []
merge_sort(A, 0, n - 1)
print(ans[k - 1] if len(ans) >= k else -1)