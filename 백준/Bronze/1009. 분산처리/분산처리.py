ls_2 = [2, 4, 8, 6]
ls_3 = [3, 9, 7, 1]
ls_4 = [4, 6]
ls_7 = [7, 9, 3, 1]
ls_8 = [8, 4, 2, 6]
ls_9 = [9, 1]

for _ in range(int(input())):
    a, b = map(int, input().split())
    t = a % 10
    if t == 1 or t == 5 or t == 6: print(t)
    elif t == 2:
        s = b % 4 - 1 if b % 4 else 3
        print(ls_2[s])
    elif t == 3:
        s = b % 4 - 1 if b % 4 else 3
        print(ls_3[s])
    elif t == 4:
        s = b % 2 - 1 if b % 2 else 1
        print(ls_4[s])
    elif t == 7:
        s = b % 4 - 1 if b % 4 else 3
        print(ls_7[s])
    elif t == 8:
        s = b % 4 - 1 if b % 4 else 3
        print(ls_8[s])
    elif t == 9:
        s = b % 2 - 1 if b % 2 else 1
        print(ls_9[s])
    else: print(10)