n, b = input().split()
b = int(b)
ans, order = 0, 0
for i in n[::-1]:
    if i.isdigit():
        ans += int(i) * b**order
    else:
        ans += (ord(i)-55) * b**order
    order += 1
print(ans)