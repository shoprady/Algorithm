for _ in range(int(input())):
    ls = list(map(int, input().split()))
    aver = (sum(ls) - ls[0]) / ls[0]
    ans = 0
    for i in range(1, ls[0]+1):
        if ls[i] > aver:
            ans += 1
    print(f'{ans/ls[0]*100:.3f}%')