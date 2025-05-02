check = int(input()) <= 50
n = int(input())
if n <= 10:
    if check: ans = 'White'
    else: ans = 'Yellow'
elif n > 30: ans = 'Red'
else: ans = 'Yellow'
print(ans)