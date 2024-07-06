n, k = map(int, input().split())
list = [i for i in range(1, n + 1) if n % i == 0]

if len(list) < k:
    print(0)
else:
    print(list[k - 1])