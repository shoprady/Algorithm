a, b, c = map(int, input().split())
def power(x, y):
    if y == 0: return 1
    z = power(x, y // 2)
    if y % 2 == 0: return z * z % c
    else: return a * z * z % c
print(power(a, b))