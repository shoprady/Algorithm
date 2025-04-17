def get_ans(ls):
    tmp, ans, prev = 0, 0, 0
    for i in ls:
        tmp = max(i, tmp)
        if i == tmp and i != prev: ans += 1
        prev = tmp
    return ans

ls = []
for _ in range(int(input())):
    ls.append(int(input()))
print(get_ans(ls))
print(get_ans(ls[::-1]))