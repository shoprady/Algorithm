t, score, ans = int(input()), list(map(int, input().split())), 0
if t < 5:
    score.extend([0] * (5 - t))
if score[0] > score[2]:
    ans += (score[0] - score[2]) * 508
else: ans += (score[2] - score[0]) * 108
if score[1] > score[3]:
    ans += (score[1] - score[3]) * 212
else: ans += (score[3] - score[1]) * 305
if score[4]: ans += score[4] * 707
print(ans * 4763)