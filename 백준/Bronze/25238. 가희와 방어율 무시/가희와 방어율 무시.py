a, b = map(int, input().split())
print(1 * (a * (100 - b) // 100 < 100))