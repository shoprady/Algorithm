x, n = map(int, input().split())
time = 0
while time < n:
    if x % 2 == 0: x = (x // 2) ^ 6
    else: x = (2 * x) ^ 6
    time += 1
print(x)