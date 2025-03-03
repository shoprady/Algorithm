f = input()
nums, tmp = [], ''
for i in f:
    if i.isdigit():
        tmp += i
    else:
        nums.append(int(tmp))
        tmp = '' if i == '+' else '-'
nums.append(int(tmp))

ans, minus = 0, False
for i in range(len(nums)):
    if nums[i] >= 0:
        if minus: ans -= nums[i]
        else: ans += nums[i]
    else:
        if minus:
            ans += nums[i]
        else:
            minus = True
            ans += nums[i]
print(ans)