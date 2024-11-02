k = int(input())
nums = []
for _ in range(k):
    n = int(input())
    if n == 0:
        if not nums: continue
        else: nums.pop()
    else: nums.append(n)
print(sum(nums))