n = int(input())
nums = [[0] * n for _ in range(3)]
for i in range(n):
    a, b, c = map(int, input().split())
    nums[0][i] += a
    nums[1][i] += b
    nums[2][i] += c
ans = [0] * n
for k in range(3):
    for i in range(n):
        check = True
        for j in range(n):
            if i != j and nums[k][i] == nums[k][j]: check = False
        ans[i] += nums[k][i] if check else 0
for i in ans:
    print(i)