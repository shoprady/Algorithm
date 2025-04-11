ls = sorted(list(map(int, input().split())))
diff = min(ls[1] - ls[0], ls[2] - ls[1])
for i in range(3):
    if ls[i] + diff not in ls:
        print(ls[i] + diff)