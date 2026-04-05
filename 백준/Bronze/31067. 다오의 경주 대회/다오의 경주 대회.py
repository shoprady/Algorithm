n, k = map(int, input().split())
ls = list(map(int, input().split()))
ans = 0
for i in range(n-1):
    if ls[i+1] > ls[i]:
        continue
    elif ls[i+1]+k <= ls[i]:
        ans = -1
        break
    else:
        ls[i+1] += k
        ans += 1
print(ans)