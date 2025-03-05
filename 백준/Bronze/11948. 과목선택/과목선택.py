a, b = [], []
for _ in range(4):
    a.append(int(input()))
for _ in range(2):
    b.append(int(input()))

ans = max(a)
for _ in range(2):
    a.remove(max(a))
    ans += max(a)
print(ans + max(b))