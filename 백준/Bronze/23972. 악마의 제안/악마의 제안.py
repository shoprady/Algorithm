k, n = map(int, input().split())
if n == 1:
    print(-1)
elif k*n % (n-1):
    print(k*n//(n-1)+1)
else:
    print(k*n//(n-1))