n = int(input())
scores = list(map(int, input().split()))

m = max(scores)
ans_scores = [i / m * 100 for i in scores]

print(sum(ans_scores) / n)