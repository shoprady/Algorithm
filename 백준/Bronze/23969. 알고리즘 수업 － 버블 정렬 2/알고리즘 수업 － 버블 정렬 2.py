def bubble_sort(A, n, k):
    order = 0
    for last in range(n, 1, -1):
        for i in range(last - 1):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                order += 1
            if order == k:
                for a in A: print(a, end=' ')
                return
    return print(-1)
                
n, k = map(int, input().split())
A = list(map(int, input().split()))
bubble_sort(A, n, k)