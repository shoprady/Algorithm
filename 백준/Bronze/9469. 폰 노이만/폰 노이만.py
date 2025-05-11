for _ in range(int(input())):
    n, d, a, b, f = map(float, input().split())
    v = d / (a + b)
    print(f'{int(n)} {v * f:.6f}')