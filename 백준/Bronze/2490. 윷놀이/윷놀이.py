for _ in range(3):
    ans = sum(map(int, input().split()))
    if ans == 3: print('A')
    elif ans == 2: print('B')
    elif ans == 1: print('C')
    elif ans == 0: print('D')
    else: print('E')