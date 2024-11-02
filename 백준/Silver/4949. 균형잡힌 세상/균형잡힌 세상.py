while True:
    s = input()
    if s == '.':
        break
    
    check, stack = 'no', []
    for ch in s:
        if ch in '([':
            stack.append(ch)
        if ch in ')]':
            if not stack:
                check = 'no'
                break
            else:
                left = stack[-1]
                if (left == '(' and ch == ')') or (left == '[' and ch == ']'):
                    stack.pop()
                else:
                    check = 'no'
                    break
                
    if not stack and ch not in ')]':
        check = 'yes'
    print(check)