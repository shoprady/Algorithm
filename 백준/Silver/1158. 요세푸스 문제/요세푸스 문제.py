from collections import deque

n, k = map(int, input().split())
queue = deque(range(1, n + 1))

nums = []
while queue:
    queue.rotate(-k+1)
    nums.append(queue.popleft())

print('<', end='')
for i in range(len(nums)):
    if i < len(nums) - 1:
        print(nums[i], end=', ')
    else:
        print(nums[i], end='')
print('>')