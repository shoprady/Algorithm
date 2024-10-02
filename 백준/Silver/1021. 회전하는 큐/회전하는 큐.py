from collections import deque

n, m = map(int, input().split())
delete_nums = list(map(int, input().split()))
nums = deque(range(1, n + 1))

count = 0
for num in delete_nums:
    if nums[0] == num:
        nums.popleft()
        n -= 1
        continue

    if nums.index(num) > n/2:
        move = n - nums.index(num)
    else:
        move = - nums.index(num)
    nums.rotate(move); nums.popleft()
    count += abs(move)
    n -= 1
        
print(count)