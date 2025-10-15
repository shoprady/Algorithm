n = int(input())
car = int(input())
ans = car
for _ in range(n):
    a, b = map(int, input().split())
    car = car + a - b
    if car < 0:
        ans = 0
        break
    ans = max(car, ans)
print(ans)