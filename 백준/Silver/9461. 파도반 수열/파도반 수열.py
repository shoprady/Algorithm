t = int(input())    
nums = [0, 1, 1, 1, 2]
for i in range(5, 101):
    nums.append(nums[i - 1] + nums[i - 5])
for _ in range(t):
    print(nums[int(input())])