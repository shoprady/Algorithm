n = int(input())
ls = list(map(int, input().split()))
a, anger = 0, []
for i in ls:
    if i: a += 1
    else: a -= 1
    anger.append(a)
print(sum(anger))