n = int(input())
if n % 2 == 0: n //= 2
else: n = n // 2 + 1

ls = list(map(int, input().split()))
dic = dict()
for i in ls:
    if i in dic: dic[i] += 1
    else: dic[i] = 1

check = True
for i in dic:
    if dic[i] > n: check = False
print('YES') if check else print('NO')