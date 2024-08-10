n = int(input())
ans = 0

for i in range(1, n):
    i_sum = i
    i_digits = list(map(int, list(str(i))))
    for digit in i_digits:
        i_sum += digit
    if i_sum == n:
        ans = i
        break
        
print(ans)