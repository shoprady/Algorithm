ans = 0
for _ in range(int(input())):
    ls, tmp = list(map(int, input().split())), 0
    run, trick = ls[:2], sorted(ls[2:])
    tmp += max(run) + trick[-1] + trick[-2]
    if tmp > ans:
        ans = tmp
print(ans)