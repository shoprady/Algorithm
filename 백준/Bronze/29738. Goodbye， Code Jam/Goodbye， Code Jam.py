for i in range(int(input())):
    y = int(input())
    if y > 4500: print("Case #{0}: Round 1".format(i + 1))
    elif 1000 < y <= 4500: print("Case #{0}: Round 2".format(i + 1))
    elif 25 < y <= 1000: print("Case #{0}: Round 3".format(i + 1))
    else: print("Case #{0}: World Finals".format(i + 1))