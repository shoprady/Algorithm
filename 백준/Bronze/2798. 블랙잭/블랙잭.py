n, m = map(int, input().split())
cards = list(map(int, input().split()))
ans = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            cards_sum = cards[i] + cards[j] + cards[k]
            if cards_sum > m:
                continue
            elif cards_sum > ans:
                ans = cards_sum
                
print(ans)