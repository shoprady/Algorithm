ls = []
for _ in range(int(input())):
    a, b = input().split()
    ls.append((a, int(b)))
ls.sort(key=lambda x: (-x[1], x[0]))
print(ls[0][0])