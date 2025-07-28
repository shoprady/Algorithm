n = int(input())
tmp = int(str(n)[-1] + str(n//10 + n%10)[-1])
ans = 1
while n != tmp:
    tmp = int(str(tmp)[-1] + str(tmp//10 + tmp%10)[-1])
    ans += 1
print(ans)