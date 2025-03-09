for _ in range(int(input())):
    n = int(input())
    x, i = n // 5, n % 5
    print('++++ ' * x + '|' * i)