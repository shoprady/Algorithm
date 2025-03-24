n, check = int(input()), True
for _ in range(n):
    if check: print('* '*n); check = False
    else: print(' *'*n); check = True