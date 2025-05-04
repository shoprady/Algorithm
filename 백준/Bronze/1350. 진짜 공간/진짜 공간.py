n = int(input())
files = list(map(int, input().split()))
c = int(input())

ans = 0
for i in files:
    if i == 0:
        continue
    elif i > c:
        ans += c * (i // c + int(i % c != 0))
    else:
        ans += c
print(ans)