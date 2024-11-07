import sys
sys.setrecursionlimit(int(2e4))

def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)
        
def partition(A, p, r):
    global ans
    
    x = A[r]
    i = p - 1
    
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            ans += 1
            if ans == k:
                print(A[j], A[i]); exit(0)
            A[i], A[j] = A[j], A[i]
            
    if i + 1 != r:
        ans += 1
        if ans == k:
            print(A[r], A[i + 1]); exit(0)
        A[i + 1], A[r] = A[r], A[i + 1]
        
    return i + 1

n, k = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
quick_sort(A, 0, n - 1)
print(-1)