ls = []
for i in range(int(input())):
    num = int(input())
    if i == 0: first = num
    ls.append(num)
ls.sort()
if ls[0] == first:
    print('ez')
elif ls[-1] == first:
    print('hard')
else:
    print('?')