n, k = map(int, input().split())
elements = []
for _ in range(n):
    elements.append(list(map(int, input().split())))

A = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for w in range(1, k + 1):
        if elements[i - 1][0] > w:
            A[i][w] = A[i - 1][w]
        else:
            valWith = elements[i - 1][1] + A[i - 1][w - elements[i - 1][0]]
            valWithout = A[i - 1][w]
            A[i][w] = max(valWith, valWithout)

print(A[n][k])