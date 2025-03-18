for _ in range(3):
    ans = 0
    for _ in range(int(input())):
        ans += int(input())
    if ans > 0: print('+')
    elif ans < 0: print('-')
    else: print('0')