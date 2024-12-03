a, b, v = map(int, input().split())
ans, check = (v - a) // (a - b), (v - a) % (a - b) == 0
if check: print(ans + 1)
else: print(ans + 2)