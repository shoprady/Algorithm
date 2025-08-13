while True:
    n = int(input())
    if n == -1: break
    s, ls = 0, []
    for i in range(1, n//2+1):
        if n % i == 0:
            s += i
            ls.append(i)
    if s == n:
        print(f'{n} =', end=' ')
        for i in range(len(ls)):
            print(f'{ls[i]} +', end=' ') if i<len(ls)-1 else print(f'{ls[i]}')
    else:
        print(f'{n} is NOT perfect.')