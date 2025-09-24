n, b = map(int, input().split())
ans = []
while n > 0:
    n, a = n // b, n % b
    if a < 10:
        ans.append(str(a))
    else:
        ans.append(chr(a+55))
print(''.join(ans)[::-1])