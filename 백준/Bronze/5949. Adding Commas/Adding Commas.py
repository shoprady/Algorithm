s = input()
x, y = len(s) % 3, len(s) // 3
if not y or (not x and y == 1):
    print(s)
elif not x:
    for i in range(y):
        if i == y-1:
            print(s[i*3:i*3+3])
        else:
            print(s[i*3:i*3+3], end=',')
else:
    print(s[:x], end=',')
    for i in range(y):
        if i == y-1:
            print(s[i*3+x:i*3+3+x])
        else:
            print(s[i*3+x:i*3+3+x], end=',')