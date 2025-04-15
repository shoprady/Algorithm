ls = sorted(list(map(int, input().split())))
for i in input():
    if i == 'A': print(ls[0])
    elif i == 'B': print(ls[1])
    else: print(ls[2])