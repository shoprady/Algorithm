n = int(input())
if n == 1: print(1); exit(0)
arr = [1] * n
for i in range(1, n):
    if i % 2 == 0:
        arr[i] = 2 * arr[i - 1] - 1
    else: arr[i] = 2 * arr[i - 1] + 1
print(arr[n - 1] % 10007)