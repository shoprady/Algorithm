ma = 0
for _ in range(7):
    sem = input().split()
    if int(sem[1]) > ma:
        ans = sem[0]; ma = int(sem[1])
print(ans)