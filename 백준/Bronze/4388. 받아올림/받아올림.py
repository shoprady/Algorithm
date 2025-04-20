from itertools import zip_longest
while True:
    s = input().split()
    a, b = s[0], s[1]
    if a == b == '0': break
    ans, tmp = 0, 0
    for i, j in zip_longest(a[::-1], b[::-1], fillvalue=0):
        if int(i) + int(j) + tmp >= 10:
            ans += 1
            tmp = 1
        else: tmp = 0
    print(ans)
            