n = int(input())
x = list(map(int, input().split()))
x_set = sorted(list(set(x)))
x_dic = {x_set[i]: i for i in range(len(x_set))}
for i in x:
    print(x_dic[i], end=' ')