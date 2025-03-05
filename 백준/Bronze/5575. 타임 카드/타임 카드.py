def time(ls):
    ans = [ls[3]-ls[0], ls[4]-ls[1], ls[5]-ls[2]]
    if ans[2] < 0: ans[2] += 60; ans[1] -= 1
    if ans[1] < 0: ans[1] += 60; ans[0] -= 1
    for i in ans:
        print(i, end=' ')

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
time(a); time(b); time(c)