l = int(input())
str_list = list(input())

ans = 0
for i in range(l):
    ans += (ord(str_list[i]) - 96) * 31 ** i
print(ans % 1234567891)