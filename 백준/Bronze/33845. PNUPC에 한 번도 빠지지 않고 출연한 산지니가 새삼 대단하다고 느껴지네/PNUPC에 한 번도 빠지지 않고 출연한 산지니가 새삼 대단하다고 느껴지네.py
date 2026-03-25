s = set(input())
ls = []
for i in input():
    if i not in s: ls.append(i)
print(''.join(ls))