ans = ''
for i in range(1, 6):
    name = input()
    if 'FBI' in name:
        ans += str(i) + ' '
print(ans) if ans else print('HE GOT AWAY!')