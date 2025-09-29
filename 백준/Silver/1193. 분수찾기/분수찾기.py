n = int(input())
x, y = 0, 0
x_up, check = False, False
for i in range(n-1):
    if x == 0 and not check:
        y += 1
        x_up, check = True, True
    elif y == 0 and not check:
        x += 1
        x_up, check = False, True
    else:
        if x_up:
            x += 1; y -= 1
        else:
            x -= 1; y += 1
        check = False
print(f"{x+1}/{y+1}")