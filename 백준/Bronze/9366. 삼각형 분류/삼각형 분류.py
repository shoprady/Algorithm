for i in range(int(input())):
    ls = sorted(list(map(int, input().split())))
    if ls[2] >= ls[0] + ls[1]:
        print(f'Case #{i+1}: invalid!')
    elif ls[0] == ls[1] == ls[2]:
        print(f'Case #{i+1}: equilateral')
    elif ls[0] == ls[1]:
        print(f'Case #{i+1}: isosceles')
    elif ls[1] == ls[2]:
        print(f'Case #{i+1}: isosceles')
    else:
        print(f'Case #{i+1}: scalene')