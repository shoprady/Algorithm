n, k = map(int, input().split())
gr = [i * 100 // n for i in map(int, input().split())]
ans = []
for i in gr:
    if 0 <= i <= 4: ans.append(1)
    elif 4 < i <= 11: ans.append(2)
    elif 11 < i <= 23: ans.append(3)
    elif 23 < i <= 40: ans.append(4)
    elif 40 < i <= 60: ans.append(5)
    elif 60 < i <= 77: ans.append(6)
    elif 77 < i <= 89: ans.append(7)
    elif 89 < i <= 96: ans.append(8)
    else:  ans.append(9)
for i in ans:
    print(i, end=' ')