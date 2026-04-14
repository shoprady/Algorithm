n,m = map(int, input().split())
if n != m:
    i = min(n,m) - 1
    print(i**2)
else:
    i = n-1
    a = i**2 - (i-1)*2
    b = (i**2)//2
    c = (i-1)**2
    print(max(a,b,c))