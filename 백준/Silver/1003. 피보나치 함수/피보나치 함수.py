t = int(input())
for _ in range(t):
    n = int(input())
    if n == 0: print(1, 0); continue
    elif n == 1: print(0, 1); continue
    arr = [[0, 0] for _ in range(n + 1)]
    arr[0][0], arr[1][1] = 1, 1
    for i in range(2, n + 1):
        arr[i][0] = arr[i - 2][0] + arr[i - 1][0]
        arr[i][1] = arr[i - 2][1] + arr[i - 1][1]
    print(arr[n][0], arr[n][1])