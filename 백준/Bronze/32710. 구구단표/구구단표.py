arr = set([1])
for i in range(2, 10):
    for j in range(1, 10):
        arr.add(i * j)
print(1 * (int(input()) in arr))