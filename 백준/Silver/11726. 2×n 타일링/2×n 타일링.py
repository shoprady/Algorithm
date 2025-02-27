n = int(input())
if n == 1: print(1); exit(0)
elif n == 2: print(2); exit(0)
arr = [0] * n
arr[0], arr[1] = 1, 2
for i in range(2, n):
    arr[i] = arr[i - 1] + arr[i - 2]
print(arr[n - 1] % 10007)