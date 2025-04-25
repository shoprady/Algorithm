while True:
    ls = sorted(list(map(int, input().split())))
    a, b, c = ls[0], ls[1], ls[2]
    if a == b == c == 0: break
    if c >= a + b: print('Invalid')
    elif a == b == c: print('Equilateral')
    elif a == b or b == c or a == c: print('Isosceles')
    else: print('Scalene')