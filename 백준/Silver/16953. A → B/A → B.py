a, b = map(int, input().split())
ans = 1
while True:
    if a == b:
        print(ans); break
    if a > b:
        print(-1); break
        
    if b % 2 == 0:
        b //= 2; ans += 1
    elif b % 10 == 1:
        b = (b - 1) // 10; ans += 1
    else: print(-1); break