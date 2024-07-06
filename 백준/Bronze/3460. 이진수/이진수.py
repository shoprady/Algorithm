T = int(input())
for _ in range(T):
    n = int(input())
    order = 0
    while n > 0:
        if n % 2 == 1:
            print(order, end=" ")
        n = n // 2
        order += 1