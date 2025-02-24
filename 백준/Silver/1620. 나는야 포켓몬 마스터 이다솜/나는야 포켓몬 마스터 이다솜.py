import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
dic, rev_dic = dict(), dict()
for i in range(1, n + 1):
    name = sys.stdin.readline().rstrip()
    dic[str(i)] = name
    rev_dic[name] = str(i)
for _ in range(m):
    order = input()
    if order.isalpha():
        print(rev_dic[order])
    else:
        print(dic[order])