order = input()
ans = 1
for i in order:
    if i == 'A':
        if ans == 1: ans = 2
        elif ans == 2: ans = 1
    elif i == 'B':
        if ans == 2: ans = 3
        elif ans == 3: ans = 2
    else:
        if ans == 3: ans = 1
        elif ans == 1: ans = 3
print(ans)