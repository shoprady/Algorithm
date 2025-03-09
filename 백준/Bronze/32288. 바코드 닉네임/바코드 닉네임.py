n, nick = int(input()), list(input())
for i in range(n):
    if nick[i].isupper(): nick[i] = nick[i].lower()
    else: nick[i] = nick[i].upper()
print(''.join(nick))