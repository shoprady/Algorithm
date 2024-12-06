from collections import deque
n = int(input())

nums = deque()
for i in range(n):
    nums.append(i + 1)

while len(nums) > 1:
    # 1
    nums.popleft()
    # 2
    i = nums.popleft()
    nums.append(i)

print(nums[0])