scores = []
for _ in range(5):
    n = int(input())
    if n >= 40: scores.append(n)
    else: scores.append(40)
print(sum(scores) // 5)