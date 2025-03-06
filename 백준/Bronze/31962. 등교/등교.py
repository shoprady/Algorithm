n, x = map(int, input().split())
ma = 0
for i in range(n):
    bus = list(map(int, input().split()))
    if sum(bus) <= x:
        ma = max(bus[0], ma)
if ma == 0: print(-1)
else: print(ma)