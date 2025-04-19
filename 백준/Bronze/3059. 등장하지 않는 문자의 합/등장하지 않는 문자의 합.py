for _ in range(int(input())):
    s, ans = input(), 0
    for i in range(65, 91):
        if chr(i) not in s:
            ans += i
    print(ans)