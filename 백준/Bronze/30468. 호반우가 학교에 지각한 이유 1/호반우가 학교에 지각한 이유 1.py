ls = list(map(int, input().split()))
curr, n4 = sum(ls) - ls[4], ls[4] * 4
if curr < n4: print(n4 - curr)
else: print(0)