tmp = []
for _ in range(5):
    tmp.append(int(input()))
if tmp[0] > 0:
    print((tmp[1] - tmp[0]) * tmp[4])
else:
    print(-tmp[0] * tmp[2] + tmp[1] * tmp[4] + tmp[3])