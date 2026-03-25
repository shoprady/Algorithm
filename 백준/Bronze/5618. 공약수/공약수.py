n = int(input())
if n == 2:
    a, b = map(int, input().split())
    for i in range(1, 1+min(a,b)):
        if a%i==0 and b%i==0: print(i)
else:
    ans = []
    a, b, c = map(int, input().split())
    for i in range(1, 1+min(a,b)):
        if a%i==0 and b%i==0: ans.append(i)
    for i in ans:
        if b%i or c%i: ans.remove(i)
    for i in ans:
        if c%i or a%i: ans.remove(i)
    for i in ans:
        print(i)