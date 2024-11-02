n = int(input())
stack, ans, check = [], [], True
order = 1
for _ in range(n):
    num = int(input())
    while order <= num:
        stack.append(order)
        ans.append('+')
        order += 1
    if num == stack[-1]:
        stack.pop()
        ans.append('-')
    elif num in stack:
        check = False
        break
        
if check:
    for i in ans: print(i)
else:
    print("NO")