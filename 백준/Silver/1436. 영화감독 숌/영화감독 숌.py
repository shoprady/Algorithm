n = int(input())
ans, order = 0, 0
while True:
    ans += 1
    if '666' in str(ans):
        order += 1
        if order == n: break
print(str(ans))