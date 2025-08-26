n, score, p = map(int, input().split())
if n == 0:
    print(1)
    exit(0)
ls = list(map(int, input().split()))
if n == p and score <= min(ls):
    print(-1)
elif n == 1:
    print(int(ls[0]>score)+1)
elif score in ls:
    print(ls.index(score)+1)
else:
    check = True
    for i in range(n-1):
        if ls[i+1] <= score <= ls[i]:
            print(i+2)
            check = False
        if check and i==n-2:
            print(n+1)