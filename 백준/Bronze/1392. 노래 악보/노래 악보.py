n, q = map(int, input().split())
ls, i = [], 1
for _ in range(n):
    k = int(input())
    ls.extend([i] * k)
    i += 1
for _ in range(q):
    print(ls[int(input())])