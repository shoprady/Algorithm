n, m = map(int, input().split())
dic = dict()
for _ in range(n):
    ls = input().split()
    dic[ls[0]] = ls[1]
for _ in range(m):
    print(dic[input()])