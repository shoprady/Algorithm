n = int(input())
tmp = list(input())
for _ in range(n - 1):
    s = list(input())
    for i in range(len(tmp)):
        if tmp[i] != s[i] and tmp[i] != '?':
            tmp[i] = '?'
print(''.join(tmp))