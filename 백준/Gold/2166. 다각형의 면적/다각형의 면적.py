ls = []
for _ in range(int(input())):
    ls.append(list(map(int, input().split())))
a, b = 0, 0
for i in range(len(ls)):
    if i < len(ls)-1:
        a += ls[i][0] * ls[i+1][1]
        b += ls[i+1][0] * ls[i][1]
    else:
        a += ls[i][0] * ls[0][1]
        b += ls[0][0] * ls[i][1]
print(0.5 * abs(a-b))