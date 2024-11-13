n = int(input())
ch_dict = {}

for _ in range(n):
    name = input()
    try:
        ch_dict[name[0]] += 1
    except:
        ch_dict[name[0]] = 1

check, ans = False, ''
for ch in ch_dict:
    if ch_dict[ch] >= 5:
        check = True
        ans += ch
        
if check:
    print(''.join(sorted(ans)))
else: print("PREDAJA")