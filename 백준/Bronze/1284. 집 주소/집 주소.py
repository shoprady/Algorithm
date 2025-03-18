while True:
    s = input()
    if s == '0': break
    ans = 0
    for i in list(s):
        if i == '0': ans += 4
        elif i == '1': ans += 2
        else: ans += 3
    print(ans + len(s) + 1)