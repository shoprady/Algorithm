dic = {'a':0, 'i':0, 'u':0, 'e':0, 'o':0,
      'A':0, 'I':0, 'U':0, 'E':0, 'O':0}
while True:
    s, ans = input(), 0
    if s == '#': break
    for i in s:
        if i in dic: ans += 1
    print(ans)