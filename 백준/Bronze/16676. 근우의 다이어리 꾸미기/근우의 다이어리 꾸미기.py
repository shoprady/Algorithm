n = int(input())
if n == 0:
    print(1); exit(0)

p = 1
while True:
    q = int(str(p)+'1')
    if p <= n < q:
        print(len(str(p))); break
    else:
        p = q