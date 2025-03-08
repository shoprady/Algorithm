x, total = int(input()), 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    total += a * b
print('Yes') if total == x else print('No')