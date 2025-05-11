while True:
    s = input()
    if s == '#': break
    ls = [0] * 26
    for i in s:
        if 65 <= ord(i) <= 90:
            ls[ord(i)-65] = 1
        elif 97 <= ord(i) <= 122:
            ls[ord(i)-97] = 1
    print(sum(ls))