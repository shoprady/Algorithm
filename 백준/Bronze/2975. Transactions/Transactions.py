while True:
    ls = input()
    if ls == '0 W 0': break
    ls = ls.split()
    if ls[1] == 'W':
        d = int(ls[0]) - int(ls[2])
        print(d) if d >= -200 else print('Not allowed')
    else:
        print(int(ls[0]) + int(ls[2]))