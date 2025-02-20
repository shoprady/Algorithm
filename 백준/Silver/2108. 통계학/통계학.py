import math

n = int(input())
nums, dic = [], dict()
for i in range(n):
    nums.append(int(input()))
    if nums[i] in dic:
        dic[nums[i]] += 1
    else: dic[nums[i]] = 1

print(math.floor(sum(nums) / n + 0.5))
print(sorted(nums)[n // 2])

mod = max(dic.values())
mod_nums = []
for i in dic:
    if dic[i] == mod:
        mod_nums.append(i)
if len(mod_nums) == 1:
    print(mod_nums[0])
else: print(sorted(mod_nums)[1])

print(max(nums) - min(nums))