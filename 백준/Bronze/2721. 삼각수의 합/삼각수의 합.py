for _ in range(int(input())):
    w = 0
    for i in range(1, int(input()) + 1):
        w += i * sum([j for j in range(1, i + 2)])
    print(w)