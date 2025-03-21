while True:
    ls = list(map(int, input().split()))
    if ls[0] == 0: break
    leaf = 1
    for i in range(1, 2 * ls[0], 2):
        leaf = leaf * ls[i] - ls[i + 1]
    print(leaf)