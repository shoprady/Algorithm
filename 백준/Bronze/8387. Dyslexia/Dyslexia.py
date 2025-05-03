n = int(input())
l1, l2 = list(input()), list(input())
ans = 0
for i in range(n):
    if l1[i] == l2[i]: ans += 1
print(ans)