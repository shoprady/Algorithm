n = int(input())
st = input()
i, b, s = 0, 0, 0
for _ in range(n):
    if st[i] == 'b':
        b += 1
        i += 7
    else:
        s += 1
        i += 8
if b > s:
    print('bigdata?')
elif s > b:
    print('security!')
else:
    print('bigdata? security!')