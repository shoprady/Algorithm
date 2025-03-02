n = int(input())
a1, a2 = 0, 0
for i in range(1, n + 1):
    a1 += i
    a2 += i ** 3
print(a1); print(a1 ** 2); print(a2)