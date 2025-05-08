n, l = map(int, input().split())
i = 1
while n > 0:
    if str(l) not in str(i):
        n -= 1
    i += 1
print(i-1)