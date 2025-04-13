ls_1, ls_2 = [], []
ans_a, ans_b = 0, 0
for _ in range(3):
    a, b = map(int, input().split())
    ls_1.append(a)
    ls_2.append(b)
for i in range(3):
    a, b = ls_1[i], ls_2[i]
    if ls_1.count(a) == 1: ans_a = a
    if ls_2.count(b) == 1: ans_b = b
print(ans_a, ans_b)