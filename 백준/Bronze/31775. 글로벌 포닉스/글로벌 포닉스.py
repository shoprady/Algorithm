g = ['l', 'k', 'p']
for _ in range(3):
    s = input()
    if s[0] in g:
        g.remove(s[0])
    else:
        print('PONIX'); exit(0)
print('GLOBAL')