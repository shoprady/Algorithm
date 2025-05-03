a, b = map(lambda x: list(map(int, list(x)[::-1])), input().split())
carry, ans, i = 0, [], 0
while i < len(a) and i < len(b):
    k = a[i] + b[i] + carry
    if k == 0:
        ans.append(0)
        carry = 0
    elif k == 1:
        ans.append(1)
        carry = 0
    elif k == 2:
        ans.append(0)
        carry = 1
    else:
        ans.append(1)
        carry = 1
    i += 1
while i < len(a):
    k = a[i] + carry
    if k == 0:
        ans.append(0)
        carry = 0
    elif k == 1:
        ans.append(1)
        carry = 0
    else:
        ans.append(0)
        carry = 1
    i += 1
while i < len(b):
    k = b[i] + carry
    if k == 0:
        ans.append(0)
        carry = 0
    elif k == 1:
        ans.append(1)
        carry = 0
    else:
        ans.append(0)
        carry = 1
    i += 1
if carry: ans.append(1)
while ans[-1] == 0 and len(ans) > 1:
    ans.pop()
for i in ans[::-1]:
    print(i, end='')