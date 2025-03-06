money = sum(map(int, input().split()))
chick = int(input())
if money >= 2 * chick: print(money - 2 * chick)
else: print(money)