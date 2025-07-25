a, b = int(input()), int(input())
if a > b + 60:
    print((b + 60) * 1500 + (a - b - 60) * 3000)
else:
    print(a * 1500)