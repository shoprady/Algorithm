a, b, c = map(int, input().split())
ans = 0
while not (c == b + 1 and b == a + 1):
    if b - a > c - b: c = b
    else: a = b
    b = a + 1
    ans += 1
print(ans)