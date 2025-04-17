n = int(input()) - 1
if n < 0:
    print(0)
else:
    print(n * (n-1) * (n-2) // 6)