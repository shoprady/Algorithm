for _ in range(int(input())):
    ls = input().split()
    if ls[1] == 'kg':
        print('{:.4f} lb'.format(float(ls[0]) * 2.2046))
    elif ls[1] == 'lb':
        print('{:.4f} kg'.format(float(ls[0]) * 0.4536))
    elif ls[1] == 'l':
        print('{:.4f} g'.format(float(ls[0]) * 0.2642))
    else:
        print('{:.4f} l'.format(float(ls[0]) * 3.7854))