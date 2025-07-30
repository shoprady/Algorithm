while True:
    n = int(input())
    if n == 0: break
    ls = list(map(int, input().split()))
    m, j = ls.count(0), ls.count(1)
    print(f'Mary won {m} times and John won {j} times')