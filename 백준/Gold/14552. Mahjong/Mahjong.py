ls = list(map(int, input().split()))
idx = [0] * 10
for i in ls:
    idx[i] += 1

def check(idx, head, body, n):
    if head == 1 and body == 4:
        return True    

    while n < 10:
        if idx[n] > 0:
            if idx[n] == 3 and body < 4:
                idx[n] -= 3
                if check(idx, head, body+1, n):
                    return True
                else:
                    idx[n] += 3
            if idx[n] >= 2 and head == 0:
                idx[n] -= 2
                if check(idx, head+1, body, n):
                    return True
                else:
                    idx[n] += 2
            if n <= 7 and idx[n+1] and idx[n+2]:
                idx[n] -= 1; idx[n+1] -= 1; idx[n+2] -= 1
                if check(idx, head, body+1, n):
                    return True
                else:
                    idx[n] += 1; idx[n+1] += 1; idx[n+2] += 1
            return False
        else:
            n += 1

ans = []
for i in range(1, 10):
    if idx[i] == 4:
        continue
    else:
        idx2 = idx[:]
        idx2[i] += 1
        if idx2.count(2) == 7 or check(idx2, 0, 0, 1):
            ans.append(i)
print(*ans) if ans else print(-1)