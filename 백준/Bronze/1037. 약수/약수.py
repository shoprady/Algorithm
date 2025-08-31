n = int(input())
if n == 1: print(int(input()) ** 2)
else:
    ls = list(map(int, input().split()))
    print(min(ls) * max(ls))