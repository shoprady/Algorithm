for _ in range(int(input())):
    ans, tmp = '', ''
    for i in input():
        if i != tmp:
            ans += i
        tmp = i
    print(ans)