k = int(input())
s = input()
ls, i = [], 0
while i < len(s):
    tmp = []
    if (i // k) % 2 == 0:
        for j in range(k):
            tmp.append(s[i+j])
    else:
        for j in range(k-1, -1, -1):
            tmp.append(s[i+j])
    ls.append(tmp)
    i += k
for c in zip(*ls):
    print(''.join(c), end='')