ls = list(map(int, input().split()))
compare = [1, 1, 2, 2, 2, 8]
for i in range(6):
    if ls[i] == compare[i]:
        print(0, end=' ')
    else: print(compare[i] - ls[i], end=' ')