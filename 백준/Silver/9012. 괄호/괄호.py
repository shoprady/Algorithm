t = int(input())
for _ in range(t):
    s = input()
    stack, check = [], True
    for l in s:
        if l == '(':
            stack.append(l)
        else:
            if not stack: check = False
            else: stack.pop()
    if check and not stack: print('YES')
    else: print('NO')