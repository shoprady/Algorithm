ls = []
for _ in range(5):
    ls.append(int(input()))
print(min(ls[0] * ls[4], ls[1] + max(0, ls[4] - ls[2]) * ls[3]))