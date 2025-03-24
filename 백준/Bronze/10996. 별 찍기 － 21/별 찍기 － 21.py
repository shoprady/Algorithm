n, check = int(input()), True
for i in range(2 * n):
    if check:
        print('* ' * ((n+1)//2)); check = False
    else:
        print(' *' * (n//2)); check = True