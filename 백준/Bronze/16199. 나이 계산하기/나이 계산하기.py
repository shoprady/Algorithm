b = list(map(int, input().split()))
c = list(map(int, input().split()))

print(c[0] - b[0] - 1 + 1 * (c[1]>b[1] or (c[1]==b[1] and c[2]>=b[2])))
print(c[0] - b[0] + 1)
print(c[0] - b[0])