n, ans = input(), []
for i in range(len(n)):
    ni = int(n[i])
    if ni: ans.append(ni)
    else: ans.remove(1); ans.append(10)
print(sum(ans))