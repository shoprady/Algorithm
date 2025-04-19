for _ in range(int(input())):
    a, b = input(), input()
    ans = 0
    for i, j in zip(a, b):
        if i != j: ans += 1
    print(f'Hamming distance is {ans}.')