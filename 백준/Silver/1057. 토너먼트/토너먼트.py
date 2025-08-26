n, a, b = map(int, input().split())
i = 1
while True:
    a, b = (a+1)//2, (b+1)//2
    if a == b:
        print(i)
        break
    i += 1