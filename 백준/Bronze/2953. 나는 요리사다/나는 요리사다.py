num, ans = 0, 0
for i in range(1, 6):
    i_sum = sum(map(int, input().split()))
    if ans < i_sum:
        num, ans = i, i_sum
print(num, ans)