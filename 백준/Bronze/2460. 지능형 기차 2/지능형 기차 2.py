people = 0
list = []
for _ in range(10):
    minus, plus = map(int, input().split())
    people = people - minus + plus
    list.append(people)
print(max(list))