for _ in range(int(input())):
    ls = input().split()[1:]
    print(f"Denominations: {' '.join(ls)}")
    check = True
    for i in range(len(ls)-1):
        if int(ls[i+1]) < int(ls[i])*2:
            check = False
            break
    print('Good coin denominations!\n') if check else print('Bad coin denominations!\n')