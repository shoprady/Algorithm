n = int(input())
fruits = list(map(int, input().split()))
count, kind, l, r = [0] * 10, 1, 0, 0
count[fruits[l]] = 1
while True:
    if r == n - 1:
        print(r - l + 1); break
    r += 1
    if count[fruits[r]] == 0: kind += 1
    count[fruits[r]] += 1
    if kind > 2:
        count[fruits[l]] -= 1
        if count[fruits[l]] == 0:
            kind -= 1
        l += 1