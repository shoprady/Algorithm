people, ans = 0, 0
while True:
    minus, plus = map(int, input().split())
    people = people - minus + plus
    ans = max(ans, people)
    if plus == 0: break
print(ans)