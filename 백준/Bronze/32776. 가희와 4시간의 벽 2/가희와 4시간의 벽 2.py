s = int(input())
f = sum(map(int, input().split()))
if s <= f or s <= 240: print("high speed rail")
else: print("flight")