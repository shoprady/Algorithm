p, ans = list(map(int, input().split())), 0
x, y, r = map(int, input().split())
for i in range(4):
    if p[i] == x:
        ans = i + 1; break
print(ans)