n = int(input())
stairs = [0]
for _ in range(n):
    stairs.append(int(input()))
if n == 1: print(stairs[1]); exit(0)
scores = [0] * (n + 1)
scores[1], scores[2] = stairs[1], stairs[1] + stairs[2]
for i in range(3, n + 1):
    if scores[i - 1] == scores[i - 2] + stairs[i - 1] or scores[i - 1] == scores[i - 4] + stairs[i - 2] + stairs[i - 1]:
        scores[i] = max(scores[i - 3] + stairs[i - 1] + stairs[i], scores[i - 2] + stairs[i])
    else: scores[i] = max(stairs[i] + scores[i - 1], stairs[i] + scores[i - 2])
print(scores[n]) #