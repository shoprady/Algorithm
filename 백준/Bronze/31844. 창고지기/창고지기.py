s = input()
for i in range(10):
    if s[i] == '@': rob = i
    elif s[i] == '#': box = i
    elif s[i] == '!': goal = i
if box<rob<goal or box<goal<rob or goal<rob<box or rob<goal<box: print(-1)
else: print(abs(rob-goal)-1)