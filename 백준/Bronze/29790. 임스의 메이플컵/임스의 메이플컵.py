n, u, l = map(int, input().split())
c1, c2 = n >= 1000, u >= 8000 or l >= 260
if c1 and c2: print("Very Good")
elif c1: print("Good")
else: print("Bad")