n = int(input())
cards = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

cards_dict = {}
for i in range(n):
    cards_dict[cards[i]] = i

ans = []
for num in nums:
    if num in cards_dict:
        ans.append(1)
    else: ans.append(0)
        
for i in ans:
    print(i, end=' ')