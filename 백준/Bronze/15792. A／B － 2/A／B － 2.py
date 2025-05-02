a, b = map(int, input().split())
print(a // b, end='')
if a % b:
    print('.', end='')
    for i in range(1000):
        if not a % b: break
        a = a % b * 10
        print(a // b, end='')