b, w = map(int, input().split())
ans = max(b, w)
while ans > 0:
    n = ans ** 2
    if n % 2 == 0:
        if b >= n//2 and w >= n//2:
            break
        else:
            ans -= 1
    else:
        if (b >= n//2 and w >= n//2+1) or (b >= n//2+1 and w >= n//2):
            break
        else:
            ans -= 1
print(ans) if ans > 0 else print('Impossible')